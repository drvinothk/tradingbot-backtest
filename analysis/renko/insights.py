"""Anomaly check + CE/PE split + hold-in-bricks stats for renko3c configs (engine exits)."""
import glob, os, json, statistics as st
import replay as R

CFG = "D:/TradingBot/backtest_engine/sweep_configs/renko3c_overnight_batch.txt"
params = {}
for line in open(CFG):
    if line.startswith('#') or not line.strip():
        continue
    n, _, p = line.strip().split('|', 2)
    params[n] = json.loads(p)


def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


def summ(p):
    if not p:
        return "n=0"
    ex1 = sum(sorted(p)[:-1]) if len(p) > 1 else 0
    return f"n={len(p):2} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):3.0f}% ex1={ex1:>7,.0f} avgW={st.mean([x for x in p if x>0]) if any(x>0 for x in p) else 0:>6,.0f} avgL={st.mean([x for x in p if x<=0]) if any(x<=0 for x in p) else 0:>7,.0f}"


def hold(t, B, tf):
    """bricks printed between entry and exit (favourable/adverse), source candles held, minutes held."""
    day = t['e'].date(); ev = R.renko_events(day, B, tf)
    fav = 'up' if t['ce'] else 'down'
    f = a = c = 0
    for ts in sorted(ev):
        if ts < t['e'] or ts > t['x']:
            continue
        c += 1
        for d in ev[ts][0]:
            if d == fav: f += 1
            else: a += 1
    return f, a, c, (t['x'] - t['e']).total_seconds() / 60


def ms(v):
    return f"{st.mean(v):5.1f}/{st.median(v):5.1f}" if v else "  -  "


# ---- 1. anomaly: extreme vs renko3b baseline
base = {(t['e']): t for t in R.load_trades('renko3b/renko3a_b833_r15_dyn1_current.csv')}
ext = {(t['e']): t for t in R.load_trades('renko3c/renko3c_extreme_current.csv')}
print("ANOMALY extreme vs renko3b")
print(" only in baseline:", [(str(k), base[k]['sym'], round(base[k]['pnl'])) for k in base if k not in ext])
print(" only in extreme :", [(str(k), ext[k]['sym'], round(ext[k]['pnl'])) for k in ext if k not in base])
diff = [(str(k), base[k]['sym'], round(base[k]['pnl']), round(ext[k]['pnl']), base[k]['reason'], ext[k]['reason']) for k in base if k in ext and (base[k]['x'] != ext[k]['x'] or abs(base[k]['pnl'] - ext[k]['pnl']) > 1)]
print(" same entry, different outcome:", diff)
print(" sums base/ext:", round(sum(t['pnl'] for t in base.values())), round(sum(t['pnl'] for t in ext.values())))

# ---- 2. per-config CE/PE + hold stats
files = sorted(glob.glob('renko3c/*_current.csv')) + ['renko3b/renko3a_b833_r15_dyn1_current.csv']
allhold = {}
for f in files:
    name = os.path.basename(f)[:-12]
    p = params.get(name, {})
    B = p.get('fixed_brick_size_points', 8.33); tf = p.get('brick_source_timeframe_minutes', 15)
    T = sorted(R.load_trades(f), key=lambda t: t['e'])
    print(f"\n=== {name} (B={B}, tf={tf}m)")
    for side, sel in (('ALL', lambda t: True), ('CE', lambda t: t['ce']), ('PE', lambda t: not t['ce'])):
        S = [t for t in T if sel(t)]
        print(f"  {side:3} {summ([t['pnl'] for t in S])}")
    rows = []
    for t in T:
        if t['sym'] not in R.idx or t['e'].date() not in R.Ub:
            continue
        h = hold(t, B, tf)
        rows.append((t, h))
    for side, sel in (('ALL', lambda t: True), ('CE', lambda t: t['ce']), ('PE', lambda t: not t['ce'])):
        for lab, cond in (('win', lambda t: t['pnl'] > 0), ('loss', lambda t: t['pnl'] <= 0)):
            R_ = [h for t, h in rows if sel(t) and cond(t)]
            if not R_:
                continue
            print(f"  hold {side:3} {lab:4} n={len(R_):2} favBricks m/med={ms([h[0] for h in R_])}  advBricks={ms([h[1] for h in R_])}  candles={ms([h[2] for h in R_])}  minutes={ms([h[3] for h in R_])}")
