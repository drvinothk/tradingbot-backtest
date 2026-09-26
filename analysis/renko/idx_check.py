"""3-year UNDERLYING-only check of the 'Wednesday effect' for the Renko base config (renko6_tf5_x5_ema15tf).

Rebuilds the base entry signal on the NIFTY 1-min index bars (2023-06..2026-08, ~800 days; options only exist for the last ~1 year):
  5-min Renko 8.33pt bricks fed from 5-min candle closes, seeded at the first boundary bucket >= 09:31, confirm_bricks=2 (trailing
  same-colour run >= 2), entry on the boundary bar that printed the brick completing the run, CE if the candle close > EMA30(15-min candles,
  multi-day) and the last brick is up, PE mirror; window 09:30..14:30 (bar start); first signal of the day only.
Outcome (index points, gross): exit after 5 consecutive adverse 1-min closes (the tested candle exit) or 15:09, entry = open of the bar after the signal.
Step 1 validates the generator against the engine's 236 per-day entries (day, entry time, direction).
Step 2 reports index points by weekday / days-to-expiry / era. NOTE: index points cannot show option-structural effects (premium, gamma, spread)
-- they only test whether the SIGNAL has an index edge on Wednesdays (or on DTE 6) across 3 years.
"""
import bisect, math, statistics as st, collections, sys
from datetime import datetime, time, timedelta, date
import replay as R

B = 8.33
CONF = 2
days = sorted(d for d in R.Ub if len(R.Ub[d]) >= 300)
U = R.U


def ema_series(closes, n=30):
    out = []; k = 2 / (n + 1); e = None; buf = []
    for c in closes:
        if e is None:
            buf.append(c)
            if len(buf) == n:
                e = sum(buf) / n; out.append(e)
            else:
                out.append(None)
        else:
            e = c * k + e * (1 - k); out.append(e)
    return out


# 15-min candles (complete windows only), all days, chronological
c15_end, c15_close = [], []
for d in days:
    a0 = datetime.combine(d, time(9, 15))
    by = {ts: U[ts] for ts in R.Ub[d]}
    for i in range(25):
        ws = a0 + timedelta(minutes=15 * i)
        subs = [ws + timedelta(minutes=k) for k in range(15)]
        if all(s in by for s in subs):
            c15_end.append(ws + timedelta(minutes=15)); c15_close.append(by[subs[-1]][3])
c15_ema = ema_series(c15_close, 30)


def ema_at(t):
    i = bisect.bisect_right(c15_end, t) - 1
    return c15_ema[i] if i >= 0 else None


def first_signal(d):
    a0 = datetime.combine(d, time(9, 15))
    rs = None; bricks = []
    for ts in R.Ub[d]:
        if ((ts - a0).total_seconds() + 60) % 300 != 0 or ts.time() < time(9, 31):
            continue
        # candle must be complete (all 5 sub-bars)
        if not all((ts - timedelta(minutes=k)) in U for k in range(5)):
            continue
        c = U[ts][3]
        if rs is None:
            rs = R.RS(c, B)
        new = rs.update(c)
        bricks += new
        if not new or ts.time() > time(14, 30) or ts.time() < time(9, 30):
            continue
        last = bricks[-1]; run = 0
        for x in reversed(bricks):
            if x == last: run += 1
            else: break
        if run < CONF:
            continue
        e = ema_at(ts + timedelta(minutes=1))
        if e is None:
            continue
        if last == 'up' and c > e: return ts + timedelta(minutes=1), True
        if last == 'down' and c < e: return ts + timedelta(minutes=1), False
    return None


def outcome(d, entry, ce, n_adv=5):
    """index points after the tested candle exit"""
    if entry not in U: return None
    ep = U[entry][0]; run = 0
    for ts in R.Ub[d]:
        if ts < entry: continue
        if ts.time() >= time(15, 9):
            return (U[ts][3] - ep) * (1 if ce else -1), ts
        prev = U.get(ts - timedelta(minutes=1)); cur = U[ts]
        if prev is not None:
            adv = cur[3] < prev[3] if ce else cur[3] > prev[3]
            run = run + 1 if adv else 0
            if run >= n_adv:
                return (cur[3] - ep) * (1 if ce else -1), ts
    return None


def expiry_after(d):
    # NIFTY weekly expiry: Thursday until 2025-08-31, Tuesday from 2025-09-01 (SEBI). Holiday shifts ignored (calendar approximation).
    wd = 3 if d < date(2025, 9, 1) else 1
    return d + timedelta(days=(wd - d.weekday()) % 7)


rows = []
for d in days:
    s = first_signal(d)
    if not s: continue
    entry, ce = s
    o = outcome(d, entry, ce)
    if o is None: continue
    rows.append(dict(d=d, e=entry, ce=ce, pts=o[0], wd=d.weekday(), dte=(expiry_after(d) - d).days))
print(f"days with data {len(days)} {days[0]}..{days[-1]}; signals {len(rows)}")

# ---- step 1: validate against engine entries
eng = {}
for t in R.load_trades('perday1/pd1_base_current.csv'):
    eng[t['e'].date()] = t
match_t = match_dir = both = n_eng = 0; miss = []
mine = {r['d']: r for r in rows}
for d, t in eng.items():
    n_eng += 1
    r = mine.get(d)
    if r is None:
        miss.append((str(d), 'no signal')); continue
    same_t = r['e'] == t['e']; same_d = r['ce'] == t['ce']
    match_t += same_t; match_dir += same_d; both += same_t and same_d
    if not (same_t and same_d): miss.append((str(d), str(r['e'].time()), r['ce'], str(t['e'].time()), t['ce']))
extra = [str(d) for d in mine if d not in eng and d >= min(eng)]
print(f"VALIDATION vs engine per-day entries: {n_eng} engine trades; same entry time {match_t}, same direction {match_dir}, both {both} ({100*both/n_eng:.0f}%); my extra signals on engine-covered days without an engine trade: {len(extra)}")
print(' mismatches (first 12):', miss[:12])
# agreement of index points sign with option pnl on matched trades
agree = tot = 0
for d, t in eng.items():
    r = mine.get(d)
    if r and r['e'] == t['e'] and r['ce'] == t['ce']:
        tot += 1; agree += (r['pts'] > 0) == (t['pnl'] > 0)
print(f" sign(index pts) == sign(option pnl) on {tot} matched trades: {agree} ({100*agree/max(tot,1):.0f}%)")


def stats(lab, xs):
    if len(xs) < 2: return f"{lab:24} n={len(xs)}"
    m = st.mean(xs); s = st.stdev(xs); w = [x for x in xs if x > 0]; l = [x for x in xs if x < 0]
    return f"{lab:24} n={len(xs):3} mean={m:6.1f}pt t={m/(s/math.sqrt(len(xs))):5.2f} win={100*len(w)/len(xs):2.0f}% PF={(sum(w)/-sum(l)) if l else 9.99:4.2f} sum={sum(xs):>7,.0f}"


DN = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
eras = {'2023-06..2025-08 (Thu expiry, options n/a)': lambda r: r['d'] < date(2025, 8, 28), '2025-08-28..2026-08 (Tue expiry, options era)': lambda r: r['d'] >= date(2025, 8, 28)}
for en, ef in eras.items():
    R_ = [r for r in rows if ef(r)]
    print(f"\n=== ERA {en}: {len(R_)} trades, all {stats('', [r['pts'] for r in R_])[26:]}")
    print(" by weekday:")
    for wd in range(5): print('  ', stats(DN[wd], [r['pts'] for r in R_ if r['wd'] == wd]))
    print(" by calendar DTE:")
    for dte in sorted({r['dte'] for r in R_}): print('  ', stats(f'DTE {dte}', [r['pts'] for r in R_ if r['dte'] == dte]))
    wed = [r['pts'] for r in R_ if r['wd'] == 2]; oth = [r['pts'] for r in R_ if r['wd'] != 2]
    se = math.sqrt(st.variance(wed) / len(wed) + st.variance(oth) / len(oth))
    print(f" Wednesday vs other days: mean diff {st.mean(wed)-st.mean(oth):.1f} pt, t={(st.mean(wed)-st.mean(oth))/se:.2f}")
    d6 = [r['pts'] for r in R_ if r['dte'] == 6]; od = [r['pts'] for r in R_ if r['dte'] != 6]
    se = math.sqrt(st.variance(d6) / len(d6) + st.variance(od) / len(od))
    print(f" DTE 6 vs other days:     mean diff {st.mean(d6)-st.mean(od):.1f} pt, t={(st.mean(d6)-st.mean(od))/se:.2f}")
    print(" CE/PE:", stats('CE', [r['pts'] for r in R_ if r['ce']]), '|', stats('PE', [r['pts'] for r in R_ if not r['ce']]))

print("\n=== EXTRA: is DTE 6 ('day after expiry') stable out-of-sample?")
d6 = [r for r in rows if r['dte'] == 6]; ot = [r for r in rows if r['dte'] != 6]
print(' pooled 3y DTE6:', stats('DTE6', [r['pts'] for r in d6]), '\n pooled 3y other:', stats('other', [r['pts'] for r in ot]))
se = math.sqrt(st.variance([r['pts'] for r in d6]) / len(d6) + st.variance([r['pts'] for r in ot]) / len(ot))
print(f" pooled DTE6 - other: {st.mean([r['pts'] for r in d6])-st.mean([r['pts'] for r in ot]):.1f} pt, t={(st.mean([r['pts'] for r in d6])-st.mean([r['pts'] for r in ot]))/se:.2f}")
cuts = [date(2023, 6, 13), date(2024, 1, 1), date(2024, 7, 1), date(2025, 1, 1), date(2025, 8, 28), date(2026, 3, 1), date(2026, 9, 1)]
for a, b in zip(cuts, cuts[1:]):
    seg = [r for r in rows if a <= r['d'] < b]
    x6 = [r['pts'] for r in seg if r['dte'] == 6]; xo = [r['pts'] for r in seg if r['dte'] != 6]
    if len(x6) > 1 and len(xo) > 1: print(f" {a}..{b}: DTE6 n={len(x6)} mean={st.mean(x6):6.1f} | other n={len(xo)} mean={st.mean(xo):6.1f} | all n={len(seg)} mean={st.mean([r['pts'] for r in seg]):5.1f}")
print(' DTE6 by side pooled:', stats('CE', [r['pts'] for r in d6 if r['ce']]), '|', stats('PE', [r['pts'] for r in d6 if not r['ce']]))
# does the day-after-expiry effect exist for a NO-SIGNAL baseline (any-direction index drift)? open->15:09 move on DTE6 days
mv = collections.defaultdict(list)
for d in days:
    o = U[R.Ub[d][0]][0]; c = U[[t for t in R.Ub[d] if t.time() <= time(15, 9)][-1]][3]
    mv[(expiry_after(d) - d).days].append(c - o)
print(' index open->close mean (pts) by calendar DTE (all days, no signal):', {k: (len(v), round(st.mean(v), 1), round(st.stdev(v), 0)) for k, v in sorted(mv.items()) if len(v) > 20})
