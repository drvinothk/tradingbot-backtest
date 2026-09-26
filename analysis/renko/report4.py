"""usage: python report4.py <dir with *_current.csv> <config file> [pattern]
Engine result per config (+CE/PE split) and offline exit replays on the config's own entries:
rev1 (control), rev1+no-progress 2/3 candles, rev2, rev2+noprog. Same BR.sim as validated vs the engine."""
import glob, os, sys, json, statistics as st
import replay as R, bricks as BR
d, cfgf = sys.argv[1], sys.argv[2]; pat = sys.argv[3] if len(sys.argv) > 3 else '*'
params = {}
for line in open(cfgf):
    if line.startswith('#') or not line.strip(): continue
    n, _, p = line.strip().split('|', 2); params[n] = json.loads(p)
def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0); return w / l if l else float('inf')
def row(label, P):  # P = [(pnl, ce)]
    p = [a for a, _ in P]
    if not p: return f"  {label:24} n=0"
    ce = [a for a, c in P if c]; pe = [a for a, c in P if not c]
    return (f"  {label:24} n={len(p):2} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):3.0f}% "
            f"ex1={sum(sorted(p)[:-1]):>7,.0f} ex2={sum(sorted(p)[:-2]):>7,.0f} | CE n={len(ce):2} {sum(ce):>7,.0f} PF={pf(ce):4.2f} | PE n={len(pe):2} {sum(pe):>7,.0f} PF={pf(pe):4.2f}")
for f in sorted(glob.glob(f"{d}/{pat}_current.csv")):
    name = os.path.basename(f)[:-12]; p = params.get(name, {})
    B = p.get('fixed_brick_size_points', 8.33); tf = p.get('brick_source_timeframe_minutes', 15)
    T = sorted(R.load_trades(f), key=lambda t: t['e'])
    days = len({t['e'].date() for t in T})
    print(f"\n=== {name} B={B} tf={tf}m  mv={p.get('max_move_from_open_points')} flips={p.get('min_flips_today', 0)} dirs={p.get('allowed_directions', 'both')} "
          f"mode={p.get('direction_filter_mode')} np={p.get('no_progress_exit_candles', 0)} start={p.get('entry_start_time', '09:30')} | entry days {days}, median entry {sorted(t['e'].time() for t in T)[len(T)//2] if T else None}")
    print(row('ENGINE (as run)', [(t['pnl'], t['ce']) for t in T]))
    C = [t for t in T if t['sym'] in R.idx and t['e'].date() in R.Ub]
    def rep(**kw):
        out = []
        for t in C:
            x, xp, why = BR.sim(t, B, tf, **kw)
            if x is not None: out.append(((xp - t['ep']) * t['qty'], t['ce']))
        return out
    print(f"  (replay covers {len(C)}/{len(T)} trades)")
    print(row('replay rev1 (control)', rep()))
    print(row('replay rev1 + noprog 2', rep(noprog=2)))
    print(row('replay rev1 + noprog 3', rep(noprog=3)))
    print(row('replay rev2', rep(rev_early=2, rev_late=2)))
    print(row('replay rev2 + noprog 2', rep(rev_early=2, rev_late=2, noprog=2)))
