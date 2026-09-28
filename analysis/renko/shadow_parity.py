import sys, random, statistics as st
sys.path.insert(0, "D:/tb-shadow-renko/backend")
from datetime import datetime, time, timedelta
import replay as R
import app.modules.strategy_engine.shadow_renko as rk
B = 8.33
days = sorted(d for d in R.Ub if len(R.Ub[d]) >= 300)
print('days with >=300 bars:', len(days), days[0], days[-1])
def day_bars(d): return [(ts, *R.U[ts]) for ts in R.Ub[d] if time(9,15) <= ts.time() <= time(15,29)]
# 1) brick parity: strategy entry series (seed at first boundary label >= 09:31, RS logic) vs shadow build_renko
bad = 0; checked = 0
for d in days:
    bars = day_bars(d)
    open_at = datetime.combine(d, time(9, 15))
    for tf in (5, 15):
        st_ = None; ref = []   # reference: harness-style feed at boundary labels >= 09:31
        ref_by_end = {}
        for ts in R.Ub[d]:
            if ((ts - open_at).total_seconds() + 60) % (tf * 60) != 0 or ts.time() < time(9, 31): continue
            c = R.U[ts][3]
            if st_ is None: st_ = R.RS(c, B)
            new = st_.update(c); ref += new
            ref_by_end[ts + timedelta(minutes=1)] = (list(ref), st_.top, st_.bottom)
        for end, (dirs, top, bot) in ref_by_end.items():
            candles = rk.resample(bars, open_at, tf, end)   # finished by `end`
            s = rk.build_renko(candles, B, time(9, 30))
            got = [b.direction for b in s.bricks]
            checked += 1
            if got != dirs or abs(s.top - top) > 1e-6 or abs(s.bottom - bot) > 1e-6:
                bad += 1
                if bad <= 5: print('MISMATCH', d, tf, end.time(), len(got), len(dirs))
print(f'brick parity: {checked} (day, tf, boundary) states checked, {bad} mismatches')
# 2) EMA30 warm-up sensitivity: 6 previous days (shadow) vs 14 previous days (strategy: 20 calendar days)
def closes(d, m, upto):
    open_at = datetime.combine(d, time(9, 15))
    return [c.close for c in rk.resample(day_bars(d), open_at, m, upto)]
random.seed(1); diffs = {5: [], 15: []}
for _ in range(150):
    i = random.randrange(15, len(days)); d = days[i]
    t = datetime.combine(d, time(random.choice([10, 11, 12, 13, 14]), random.choice([0, 15, 30, 45])))
    for m in (5, 15):
        today = closes(d, m, t)
        h6 = [x for dd in days[i-6:i] for x in closes(dd, m, None)]
        h14 = [x for dd in days[i-14:i] for x in closes(dd, m, None)]
        a = rk.ema_last(h6 + today, 30); b = rk.ema_last(h14 + today, 30)
        if a is not None and b is not None: diffs[m].append(abs(a - b))
for m in diffs:
    v = sorted(diffs[m]); print(f'EMA30 {m}m |6d - 14d warm-up| pts: n={len(v)} median={st.median(v):.2f} p90={v[int(.9*len(v))]:.2f} max={v[-1]:.2f}')
