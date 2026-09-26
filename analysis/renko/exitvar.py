import json, sys, glob, os
import replay as R, bricks as BR
P = {}
for f in ('../../sweep_configs/renko5_overnight_batch.txt', '../../sweep_configs/renko6_candle_exit5_batch.txt'):
    for line in open(f):
        if line.startswith('#') or not line.strip(): continue
        n, _, p = line.strip().split('|', 2); P[n] = json.loads(p)
CFG = {  # name -> (csv, B, tf)
 'tf5_x5': 'renko6', 'tf5_x5_ema15tf': 'renko6', 'c5_x5_e5': 'renko6', 'c4_x5_e5': 'renko6',
 'b625_mv50ext': 'renko5', 'b833_mv50': 'renko5', 'b625_mv40': 'renko5'}
def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0); return w / l if l else 9.99
def run(T, B, tf, **kw):
    P_ = []
    for t in T:
        x, xp, why = BR.sim(t, B, tf, **kw)
        if x is None: continue
        P_.append(((xp - t['ep']) * t['qty'], t['ce']))
    p = [a for a, _ in P_]; h = len(p) // 2
    return (f"n={len(p):2} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):2.0f}% ex2={sum(sorted(p)[:-2]):>7,.0f} "
            f"CE={sum(a for a,c in P_ if c):>6,.0f} PE={sum(a for a,c in P_ if not c):>6,.0f} H1={sum(p[:h]):>6,.0f} H2={sum(p[h:]):>6,.0f}")
for name, d in CFG.items():
    p = P[f'{d}_{name}']; B = p['fixed_brick_size_points']; tf = p['brick_source_timeframe_minutes']
    T = sorted([t for t in R.load_trades(f'{d}/{d}_{name}_current.csv') if t['sym'] in R.idx and t['e'].date() in R.Ub], key=lambda t: t['e'])
    eng = sum(t['pnl'] for t in R.load_trades(f'{d}/{d}_{name}_current.csv'))
    print(f"\n=== {name} B={B} tf={tf} entry={p['entry_mode']} | replay covers {len(T)} trades | engine net (all) {eng:,.0f}")
    if p['entry_mode'] == 'candle_confirm':
        print(' engine-equiv (cexit5)      ', run(T, B, tf, rev_early=30, rev_late=30, cexit=5))
    elif p.get('reversal_confirm_bricks', 1) >= 30 or p.get('candle_exit_confirm'):
        print(' engine-equiv (cexit5)      ', run(T, B, tf, rev_early=30, rev_late=30, cexit=5))
    else:
        print(' engine-equiv (rev1)        ', run(T, B, tf))
    for n in (2, 3, 4, 5, 6, 7, 8, 10):
        print(f' cexit {n:2}                  ', run(T, B, tf, rev_early=30, rev_late=30, cexit=n))
    print(' brick rev1 (src tf)        ', run(T, B, tf))
    print(' brick rev2                 ', run(T, B, tf, rev_early=2, rev_late=2))
    for n in (5, 6, 7):
        print(f' cexit {n} + brick rev1       ', run(T, B, tf, cexit=n))
        print(f' cexit {n} + brick rev2       ', run(T, B, tf, rev_early=2, rev_late=2, cexit=n))
    for m in (2, 3, 4):
        print(f' cexit5 + noprog {m}          ', run(T, B, tf, rev_early=30, rev_late=30, cexit=5, noprog=m))
    print(' cexit5 + BE after 3br      ', run(T, B, tf, rev_early=30, rev_late=30, cexit=5, be_at=3))
    print(' cexit5 + target 10br       ', run(T, B, tf, rev_early=30, rev_late=30, cexit=5, target=10))
