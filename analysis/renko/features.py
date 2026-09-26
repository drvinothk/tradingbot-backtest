"""Entry-feature study: which features at the signal bar separate good from bad entries (engine entries, engine exits)."""
import statistics as st
from datetime import timedelta
import replay as R
import sigrep as S
import bricks as BR

GROUPS = {
    'tf5': ['tf5'],
    '15m pooled (base15+b625+fresh_ext)': ['base15', 'b625', 'fresh_ext'],
}


def feats(t, B, tf):
    day = t['e'].date(); ev = R.renko_events(day, B, tf)
    sbs = [k for k in ev if k <= t['e'] - timedelta(minutes=1)]
    sb = max(sbs)
    bricks = []
    for ts in sorted(ev):
        if ts > sb: break
        bricks += ev[ts][0]
    fav = 'up' if t['ce'] else 'down'
    run = 0
    for d in reversed(bricks):
        if d == fav: run += 1
        else: break
    flips = sum(1 for a, b in zip(bricks, bricks[1:]) if a != b)
    close = R.U[sb][3]
    e = S.ema_at(day, 15, 30, sb)
    d0 = R.U[R.Ub[day][0]][0]
    sign = 1 if t['ce'] else -1
    a0 = R.Ub[day][0]
    return dict(
        hour=(t['e'].hour * 60 + t['e'].minute) / 60,
        run=run,
        flips=flips,
        bricks_today=len(bricks),
        flip_rate=flips / max(1, len(bricks) - 1),
        dist_ema=(sign * (close - e) / B) if e else None,
        day_move=sign * (close - d0) / B,
        atr_ratio=(R.atr.get(sb) or 0) / B,
        candle_rng=(max(R.U[k][1] for k in R.Ub[day] if sb - timedelta(minutes=tf) < k <= sb) - min(R.U[k][2] for k in R.Ub[day] if sb - timedelta(minutes=tf) < k <= sb)) / B,
    )


def pf(p):
    w = sum(x for x in p if x > 0); l = -sum(x for x in p if x < 0)
    return w / l if l else float('inf')


if __name__ == '__main__':
    for gname, names in GROUPS.items():
        rows = []
        for n in names:
            T, B, tf = BR.load(n)
            for t in T:
                f = feats(t, B, tf); f['pnl'] = t['pnl']; f['ce'] = t['ce']; rows.append(f)
        print(f"\n### {gname}  n={len(rows)}  net={sum(r['pnl'] for r in rows):,.0f}")
        for key in ('hour', 'run', 'flips', 'flip_rate', 'bricks_today', 'dist_ema', 'day_move', 'atr_ratio', 'candle_rng'):
            R_ = [r for r in rows if r[key] is not None]
            med = st.median(r[key] for r in R_)
            lo = [r['pnl'] for r in R_ if r[key] <= med]; hi = [r['pnl'] for r in R_ if r[key] > med]
            if not lo or not hi:
                continue
            print(f"  {key:12} median={med:6.2f}  LOW n={len(lo):3} avg={st.mean(lo):>6,.0f} WR={100*sum(x>0 for x in lo)/len(lo):3.0f}% PF={pf(lo):4.2f} | HIGH n={len(hi):3} avg={st.mean(hi):>6,.0f} WR={100*sum(x>0 for x in hi)/len(hi):3.0f}% PF={pf(hi):4.2f}")
        # by side and by time-of-day bucket
        for lab, cond in (('before 10:30', lambda r: r['hour'] < 10.5), ('10:30-12:00', lambda r: 10.5 <= r['hour'] < 12), ('12:00+', lambda r: r['hour'] >= 12)):
            p = [r['pnl'] for r in rows if cond(r)]
            if p: print(f"  time {lab:13} n={len(p):3} avg={st.mean(p):>6,.0f} WR={100*sum(x>0 for x in p)/len(p):3.0f}% PF={pf(p):4.2f} net={sum(p):>7,.0f}")
        for lab, cond in (('run==2', lambda r: r['run'] == 2), ('run 3-4', lambda r: 3 <= r['run'] <= 4), ('run>=5', lambda r: r['run'] >= 5)):
            p = [r['pnl'] for r in rows if cond(r)]
            if p: print(f"  {lab:8} n={len(p):3} avg={st.mean(p):>6,.0f} WR={100*sum(x>0 for x in p)/len(p):3.0f}% PF={pf(p):4.2f}")
