"""Brick-based target / trailing exit experiments on engine entries (offline, option 1-min bars)."""
import sys, statistics as st
from datetime import time, timedelta
import replay as R

CONF = {
    'tf5': ('renko3c/renko3c_tf5_current.csv', 8.33, 5),
    'base15': ('renko3b/renko3a_b833_r15_dyn1_current.csv', 8.33, 15),
    'b625': ('renko3c/renko3c_b625_current.csv', 6.25, 15),
    'fresh_ext': ('renko3c/renko3c_fresh_ext_current.csv', 8.33, 15),
    'tf20': ('renko3c/renko3c_tf20_current.csv', 8.33, 20),
}


def load(name):
    f, B, tf = CONF[name]
    T = [t for t in R.load_trades(f) if t['sym'] in R.idx and t['e'].date() in R.Ub]
    return sorted(T, key=lambda t: t['e']), B, tf


def sim(t, B, tf, rev_early=1, rev_late=1, late_at=None, target=None, be_at=None, be_lvl=0.0, noprog=None, cap_pct=None, cexit=0):
    """Walk the option minute bars; brick events at source-candle closes.
    rev_early/rev_late: reverse bricks needed to exit (late applies once peak net favourable bricks >= late_at).
    target: exit when net favourable bricks >= target. be_at/be_lvl: once peak>=be_at, exit if option close <= entry*(1+be_lvl).
    noprog: exit at a candle close if net favourable bricks <= 0 after that many candles.
    """
    day = t['e'].date(); ev = R.renko_events(day, B, tf); ce = t['ce']; fav = 'up' if ce else 'down'
    net = peak = 0; run = 0; candles = 0; arun = 0
    last = None
    for ts, o, h, l, c in R.obars(t['sym']):
        if ts < t['e']:
            continue
        last = (ts, c)
        if ts.time() >= time(15, 9):
            return ts, c, 'eod'
        if be_at is not None and peak >= be_at and c <= t['ep'] * (1 + be_lvl):
            return ts, c, 'be'
        if ts in ev:
            candles += 1
            for d in ev[ts][0]:
                if d == fav:
                    net += 1; run = 0; peak = max(peak, net)
                else:
                    net -= 1; run += 1
                    need = rev_late if (late_at is not None and peak >= late_at) else rev_early
                    if run >= need:
                        return ts, c, 'rev'
            if target is not None and net >= target:
                return ts, c, 'target'
            if noprog is not None and candles >= noprog and peak <= 0:
                return ts, c, 'noprog'
        if cexit:
            cu = R.U.get(ts); pu = R.U.get(ts - timedelta(minutes=1))
            if cu is not None and pu is not None:
                adv = cu[3] < pu[3] if ce else cu[3] > pu[3]
                arun = arun + 1 if adv else 0
                if arun >= cexit:
                    return ts, c, 'candle'
            else:
                arun = 0
    return (last[0], last[1], 'end') if last else (None, None, 'none')


def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


def stat(T, B, tf, **kw):
    P = []
    for t in T:
        x, xp, why = sim(t, B, tf, **kw)
        if x is None:
            continue
        P.append(((xp - t['ep']) * t['qty'], t['ce']))
    p = [a for a, _ in P]; ce = [a for a, c in P if c]; pe = [a for a, c in P if not c]
    ex2 = sum(sorted(p)[:-2])
    return f"net={sum(p):>7,.0f} PF={pf(p):4.2f} ex2={ex2:>7,.0f} CE={sum(ce):>6,.0f} PE={sum(pe):>6,.0f} WR={100*sum(a>0 for a in p)/len(p):3.0f}%"


if __name__ == '__main__':
    # A. how far do trades run? peak net favourable bricks under the current exit (rev 1) and continuation odds
    print("A. peak favourable bricks reached (current exit), share of trades reaching >=k and P(k+1 | k)")
    for name in CONF:
        T, B, tf = load(name)
        peaks = []
        for t in T:
            net = peak = 0; day = t['e'].date(); ev = R.renko_events(day, B, tf); fav = 'up' if t['ce'] else 'down'
            x, _, _ = sim(t, B, tf)
            for ts in sorted(ev):
                if ts < t['e'] or ts > x: continue
                for d in ev[ts][0]:
                    net += 1 if d == fav else -1; peak = max(peak, net)
            peaks.append(peak)
        n = len(peaks)
        reach = [sum(p >= k for p in peaks) for k in range(0, 21)]
        row = ' '.join(f"{k}:{reach[k]}" for k in (1, 2, 3, 4, 6, 8, 10, 12, 15, 20))
        cond = ' '.join(f"{k}->{k+1}:{reach[k+1]/reach[k]:.2f}" for k in (1, 2, 3, 4, 6, 8, 10, 12) if reach[k])
        print(f" {name:9} n={n} reach>=k  {row}\n           P(next|k) {cond}")
    # B. exit rule variants
    for name in CONF:
        T, B, tf = load(name)
        print(f"\nB. {name} (B={B}, tf={tf}m, n={len(T)})")
        print("  current rev1           ", stat(T, B, tf))
        for k in (4, 6, 8, 10, 12):
            print(f"  target {k:2} bricks       ", stat(T, B, tf, target=k))
        for k in (3, 5, 8):
            print(f"  rev1 -> rev2 after {k} br", stat(T, B, tf, rev_late=2, late_at=k))
        for k in (3, 5, 8):
            print(f"  rev2 -> rev1 after {k} br", stat(T, B, tf, rev_early=2, rev_late=1, late_at=k))
        for k in (2, 3, 4):
            print(f"  breakeven after {k} br    ", stat(T, B, tf, be_at=k, be_lvl=0.0))
        for k in (3, 5):
            print(f"  BE+10% after {k} br      ", stat(T, B, tf, be_at=k, be_lvl=0.10))
        for m in (2, 3, 4):
            print(f"  no-progress exit {m} cndl", stat(T, B, tf, noprog=m))
