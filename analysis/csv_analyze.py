"""Stdlib-only analysis of merged backtest trade CSVs (`*_current.csv`, one row per trade). Runs anywhere (box or cloud) -- no replay/index data needed.
Usage: python csv_analyze.py FILE.csv [FILE2.csv ...]            (per-lot gross P&L as in the engine CSV; est. net subtracts COST per trade)
Prints per file: summary line (n, days, net, PF, WR, avg win/loss, maxDD, ex-top-2, halves, Sharpe/Calmar, est-net), first-trade vs re-entry,
weekday, DTE, CE/PE, exit reasons. Harness label to use in reports: "multi-trade + warm-up" for w12+ runs (see RUNBOOK_CLOUD.md).
"""
import csv
import math
import re
import statistics as st
import sys
from collections import defaultdict
from datetime import date, datetime

COST = 130.0  # est. per-trade round-trip cost (ledger formula ~130); report both gross and est-net
DN = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


def load(path):
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8')):
        e = datetime.fromisoformat(r['entry_time'])
        m = re.match(r'[A-Z]+(\d{2})(\d{2})(\d{2})', r['symbol'])
        exp = date(2000 + int(m[1]), int(m[2]), int(m[3])) if m else None
        out.append(dict(e=e, d=e.date(), pnl=float(r['pnl']), ce=r['symbol'].endswith('CE'), why=r['exit_reason'],
                        dte=(exp - e.date()).days if exp else None))
    out.sort(key=lambda t: t['e'])
    return out


def pf(p):
    w = sum(x for x in p if x > 0)
    l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


def mdd(p):
    c = pk = d = 0.0
    for a in p:
        c += a
        pk = max(pk, c)
        d = max(d, pk - c)
    return d


def line(lab, p, w=24):
    if not p:
        return f"  {lab:{w}} n=0"
    return (f"  {lab:{w}} n={len(p):4d} net={sum(p):>9,.0f} PF={pf(p):5.2f} WR={100*sum(x > 0 for x in p)/len(p):3.0f}% "
            f"avg={st.mean(p):>7,.0f} ex-best={sum(sorted(p)[:-1]):>9,.0f}")


def analyze(path):
    T = load(path)
    print(f"\n=== {path}")
    if not T:
        print("  no trades")
        return
    p = [t['pnl'] for t in T]
    days = sorted({t['d'] for t in T})
    wins = [x for x in p if x > 0]
    loss = [x for x in p if x < 0]
    daily = defaultdict(float)
    for t in T:
        daily[t['d']] += t['pnl']
    dv = [daily[d] for d in days]
    sharpe = (st.mean(dv) / st.stdev(dv) * math.sqrt(252)) if len(dv) > 2 and st.stdev(dv) > 0 else float('nan')
    dd = mdd(p)
    h = len(p) // 2
    tstat = st.mean(p) / (st.stdev(p) / math.sqrt(len(p))) if len(p) > 2 and st.stdev(p) > 0 else float('nan')
    print(f"  trades={len(p)} days_traded={len(days)} net={sum(p):,.0f} est-net(-{COST:.0f}/trade)={sum(p)-COST*len(p):,.0f} PF={pf(p):.2f} "
          f"WR={100*len(wins)/len(p):.0f}% avgW={st.mean(wins) if wins else 0:,.0f} avgL={st.mean(loss) if loss else 0:,.0f} "
          f"maxDD={dd:,.0f} Calmar={sum(p)/dd if dd else float('nan'):.2f} Sharpe(daily)={sharpe:.2f} t={tstat:.2f}")
    print(f"  ex-top-2 net={sum(sorted(p)[:-2]):,.0f}   halves: H1={sum(p[:h]):,.0f} H2={sum(p[h:]):,.0f}")
    seen = set()
    first, later = [], []
    for t in T:
        (later if t['d'] in seen else first).append(t)
        seen.add(t['d'])
    print(line('first trade of day', [t['pnl'] for t in first]))
    print(line('re-entries (#2+)', [t['pnl'] for t in later]))
    for name, S in (('ALL', T), ('FIRST', first)):
        print(f" by weekday [{name}]")
        for wd in range(5):
            print(line(DN[wd], [t['pnl'] for t in S if t['e'].weekday() == wd], 8))
    print(" by DTE [ALL] (0=expiry day, 6=day after expiry)")
    for d in sorted({t['dte'] for t in T if t['dte'] is not None}):
        print(line(f'DTE{d}', [t['pnl'] for t in T if t['dte'] == d], 8))
    print(line('CE', [t['pnl'] for t in T if t['ce']]))
    print(line('PE', [t['pnl'] for t in T if not t['ce']]))
    print(" exit reasons")
    for w in sorted({t['why'] for t in T}):
        print(line(w, [t['pnl'] for t in T if t['why'] == w]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for f in sys.argv[1:]:
        analyze(f)
