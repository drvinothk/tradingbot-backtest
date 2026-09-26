import glob, os, collections
from datetime import datetime, timedelta, time
import replay as R
def candles(day, now):
    a0 = datetime.combine(day, time(9,15)); b = {}
    for ts in R.Ub[day]:
        i = int((ts-a0).total_seconds()//300)
        if i >= 0: b.setdefault(i, []).append(ts)
    out = []
    for i in sorted(b):
        st = a0+timedelta(minutes=5*i)
        if st+timedelta(minutes=5) > now: continue
        w = sorted(b[i]); bars = [R.U[t] for t in w]
        out.append(dict(start=st, o=bars[0][0], h=max(x[1] for x in bars), l=min(x[2] for x in bars), c=bars[-1][3]))
    return out
def classify(t):
    day = t['e'].date(); now = t['e']
    if day not in R.Ub: return None
    cs = candles(day, now)
    if not cs or cs[0]['start'].time() != time(9,15): return 'NO_DATA'
    c1 = cs[0]; red = next((c for c in cs[1:] if c['c'] < c['o']), None)
    lb = R.U.get(now - timedelta(minutes=1))
    if lb is None: return 'NO_DATA'
    if red is None: return 'NO_RED_YET'
    m = lambda c: (c['h']+c['l'])/2; sd = 0.1*(red['h']-red['l'])
    lo, hi = min(m(c1), m(red)), max(m(c1), m(red)); spot = lb[3]
    if lo <= spot <= hi: return 'BETWEEN'
    if lb[2] > m(red)+sd: return 'ABOVE'
    if lb[1] < m(red)-sd: return 'BELOW'
    return 'INSIDE'
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def st(p):
    if not p: return 'n=0'
    return f"n={len(p):2} net={sum(p):>7,.0f} PF={pf(p):4.2f} ex2={sum(sorted(p)[:-2]) if len(p)>2 else 0:>7,.0f}"
CFG = ['renko5_b625_mv50ext','renko6_tf5_x5_ema15tf','renko6_tf5_x5','renko5_b833_mv50','renko5_b625_mv40','renko6_c4_x5_e5','renko6_c5_x5_e5']
for n in CFG:
    d = n[:6]; T = sorted(R.load_trades(f'{d}/{n}_current.csv'), key=lambda t: t['e'])
    for t in T:
        s = classify(t); t['st'] = s
        t['zone_ok'] = None if s in (None,'NO_DATA') else s != 'BETWEEN'
        t['trend_ok'] = None if s in (None,'NO_DATA') else (s == 'NO_RED_YET' or (s == 'ABOVE' and t['ce']) or (s == 'BELOW' and not t['ce']))
    ps = sorted(T, key=lambda t: -t['pnl'])[:2]
    print(f"\n=== {n[7:]}  ALL {st([t['pnl'] for t in T])}  states {dict(collections.Counter(t['st'] for t in T))}")
    print('  unknown (no underlying data):', st([t['pnl'] for t in T if t['st'] is None]));print('  top-2 winners:', [(str(t['e'])[:16], 'CE' if t['ce'] else 'PE', round(t['pnl']), t['st']) for t in ps])
    for lab, f in (('zone_ok', lambda t: t['zone_ok']), ('trend_ok', lambda t: t['trend_ok']), ('both', lambda t: None if t['zone_ok'] is None else (t['zone_ok'] and t['trend_ok']))):
        k = [t['pnl'] for t in T if f(t) is True]; b = [t['pnl'] for t in T if f(t) is False]
        print(f"  {lab:8} KEPT {st(k)} | BLOCKED {st(b)}")
