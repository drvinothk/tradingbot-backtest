"""Offline estimate: renko entries WITH vs WITHOUT the EMA30 guidance (first signal/day, nearest-ATM option of the near expiry,
dyn 1-brick exit, no premium trail/target). Calibrated against the engine CSV of the same config."""
import re, sys
from datetime import datetime, timedelta, time
import replay as R
import sigrep as S

sym_re = re.compile(r'NIFTY(\d\d)(\d\d)(\d\d)(\d+)(CE|PE)$')
by_exp = {}
for s in R.idx:
    m = sym_re.match(s)
    if m:
        by_exp.setdefault((2000 + int(m[1]), int(m[2]), int(m[3])), {})[(int(m[4]), m[5])] = s


def pick(day, ce, spot):
    exps = sorted(e for e in by_exp if datetime(*e).date() >= day)
    if not exps:
        return None
    strikes = by_exp[exps[0]]
    side = 'CE' if ce else 'PE'
    ks = sorted({k for k, o in strikes if o == side})
    if not ks:
        return None
    k = min(ks, key=lambda x: abs(x - spot))
    return strikes[(k, side)]


def signals_noema(day, B, tf, confirm=2, start=time(9, 30), cutoff=time(14, 30)):
    ev = R.renko_events(day, B, tf); bricks = []; out = []
    for ts in sorted(ev):
        new = ev[ts][0]; bricks += new
        if not new or not (start <= ts.time() <= cutoff) or not bricks:
            continue
        rd = bricks[-1]; run = 1
        for d in reversed(bricks[:-1]):
            if d == rd: run += 1
            else: break
        if run >= confirm and new[-1] == rd:
            out.append((ts, 'CE' if rd == 'up' else 'PE', run))
    return out


def run(B, tf, use_ema, exit_n=1, ema_period=30):
    res = []
    for day in sorted(R.Ub):
        sig = (S.signals(day, B, tf, ema_period=ema_period) if use_ema else signals_noema(day, B, tf))
        if not sig:
            continue
        ts, side, run_ = sig[0]
        ce = side == 'CE'
        sym = pick(day, ce, R.U[ts][3])
        if not sym:
            continue
        e = ts + timedelta(minutes=1)
        ob = [b for b in R.obars(sym) if b[0] == e]
        if not ob:
            continue
        t = dict(sym=sym, ce=ce, e=e, ep=ob[0][1], qty=65)
        r = R.simulate(t, B, tf, struct=('dyn', exit_n), trail=None, target_pct=None)
        if r is None or 'err' in r or r['x'] is None:
            continue
        res.append((day, ce, R.pnl(t, r), run_))
    return res


def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


def show(label, res):
    p = [x[2] for x in res]
    for side, sel in (('ALL', None), ('CE', True), ('PE', False)):
        q = [x[2] for x in res if sel is None or x[1] == sel]
        if q:
            ex2 = sum(sorted(q)[:-2]) if len(q) > 2 else 0
            print(f"  {label:9} {side:3} n={len(q):3} net={sum(q):>8,.0f} PF={pf(q):4.2f} WR={100*sum(x>0 for x in q)/len(q):3.0f}% ex2={ex2:>8,.0f}")


if __name__ == '__main__':
    for B, tf, name in ((8.33, 15, 'b833 tf15'), (8.33, 5, 'tf5'), (6.25, 15, 'b625 tf15'), (8.33, 20, 'tf20')):
        print(f"== {name}")
        show('with EMA', run(B, tf, True))
        show('NO EMA', run(B, tf, False))
