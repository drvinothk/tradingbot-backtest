"""Summarise a renko sweep dir: engine result per config + offline exit-variant replay on the config's own entries.
usage: python morning_report.py <dir with *_current.csv> [pattern]
Brick size / timeframe are read from the config name (renko3c_*): defaults 8.33/15; tf5, tf20, b625 override."""
import glob, os, sys, json, re
import replay as R
from collections import Counter

CFG = "C:/Users/drvin/Trading Bot/backtest_engine/sweep_configs/renko3c_overnight_batch.txt"
params = {}
for line in open(CFG):
    if line.startswith('#') or not line.strip():
        continue
    name, _, p = line.strip().split('|', 2)
    params[name] = json.loads(p)


def pf(p):
    w = sum(x for x in p if x > 0)
    l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


def stats(label, pnls, ce, pe, ordered):
    n = len(pnls)
    if not n:
        return f"{label:26} n=0"
    s = sorted(pnls, reverse=True)
    ex2 = sorted(pnls)[:-2] if n > 2 else pnls
    ex1 = sorted(pnls)[:-1] if n > 1 else pnls
    half = n // 2
    h1, h2 = sum(ordered[:half]), sum(ordered[half:])
    return (f"{label:26} n={n:3} net={sum(pnls):>8,.0f} PF={pf(pnls):4.2f} WR={100*sum(p > 0 for p in pnls)/n:3.0f}% "
            f"ex1={sum(ex1):>8,.0f} ex2={sum(ex2):>8,.0f}/{pf(ex2):4.2f} CE={sum(ce):>7,.0f} PE={sum(pe):>7,.0f} H1={h1:>7,.0f} H2={h2:>7,.0f}")


d = sys.argv[1]
pat = sys.argv[2] if len(sys.argv) > 2 else '*'
for f in sorted(glob.glob(f"{d}/{pat}_current.csv")):
    name = os.path.basename(f)[:-12]
    p = params.get(name, {})
    B = p.get('fixed_brick_size_points', 8.33)
    tf = p.get('brick_source_timeframe_minutes', 15)
    T = sorted(R.load_trades(f), key=lambda t: t['e'])
    pn = [t['pnl'] for t in T]
    print(f"\n=== {name}  (B={B}, tf={tf}m, rule={p.get('entry_run_rule', 'any')}, ema={p.get('ema_period', 30)}/{p.get('ema_candle_position', 'close')}, mode={p.get('entry_mode', 'breakout')})")
    print(stats('ENGINE (dyn rev n=1)', pn, [t['pnl'] for t in T if t['ce']], [t['pnl'] for t in T if not t['ce']], pn))
    print('   exits:', dict(Counter(t['reason'] for t in T)), '| entry days:', len({t['e'].date() for t in T}),
          '| median entry', sorted(t['e'].time() for t in T)[len(T) // 2] if T else None)
    variants = [('rev n=1', ('dyn', 1)), ('rev n=2', ('dyn', 2)), ('rev n=3', ('dyn', 3)),
                ('flat k=1', ('flat', 1)), ('flat k=2', ('flat', 2)), ('flat k=3', ('flat', 3)), ('hold to EOD', None)]
    for label, st in variants:
        res = []
        for t in T:
            r = R.simulate(t, B, tf, struct=st, trail=None, target_pct=None)
            if r is None or 'err' in r or r['x'] is None:
                continue
            res.append((t, R.pnl(t, r)))
        print(stats('  replay ' + label, [x[1] for x in res], [x[1] for x in res if x[0]['ce']],
                    [x[1] for x in res if not x[0]['ce']], [x[1] for x in res]) + f"   (covered {len(res)}/{len(T)})")
