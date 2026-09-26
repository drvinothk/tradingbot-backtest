---
name: project-session-handoff-renko-strategy-2026-09-22
description: "HAND-OFF 2026-09-22/23: new Modified Renko trend-following strategy built, QC'd, sweep #1 (9 configs) running on A1; sweep #2 (18 configs, fixed-brick/EMA-crossover/reversal-exit variant) built+QC'd but NOT launched. Start here in the morning session."
metadata:
  type: project
  originSessionId: current
  modified: 2026-09-22T20:42:22.739Z
---

**Start here.** User asked for a Renko-based intraday (not scalping) option-buying
strategy from two research docs, evaluated + built + QC'd it, then asked for a
second variant mid-sweep. Session ended with sweep #1 still running on the box
and sweep #2 saved but deliberately not launched -- user wants to analyze
results first in a fresh morning session.

## What was built

New strategy `renko_trend`, backend-only, **on branch `wip/renko-trend-strategy`
(NOT merged to main)**, based off main `d39c62d`. Commits (in order):
`21bb3c0` (core strategy), `58cab70` (Guard 1 allowlist fix), `b2f3a35` (fixed-
brick/EMA-crossover/reversal-exit extension), plus `289f0cc` which is main's own
`d7d92d9` docs commit that landed on this branch's tip too (unrelated, harmless
— another concurrent session's work, not mine).

Files: `backend/app/modules/strategy_engine/renko.py` (pure brick engine —
`RenkoState`, `trend_run_direction`, `compute_fib_levels`,
`resample_multi_day_htf`), `backend/app/modules/strategy_engine/higher_timeframe.py`
(ported from the separate, older `wip/id-ema-thread` branch as a dependency —
`resample_to_htf`/`compute_atr_series`/`compute_ema_series`/`is_htf_boundary_close`),
`backend/app/modules/strategy_engine/strategies/renko_trend.py` (the Strategy
class itself — read its own module docstring first, it's thorough), tests in
`backend/tests/unit/test_renko.py` + `test_higher_timeframe.py` +
`backend/tests/integration/test_renko_trend_strategy.py` (27 tests, all
passing). Wired into `strategies/__init__.py`, `api/v1/strategies.py`
(`_build_strategy`/`KNOWN_STRATEGY_TYPES`/`RENKO_TREND_PARAM_KEYS`),
`scripts/run_backtest.py`'s `STRATEGY_TYPES` tuple, and
`risk_engine/service.py`'s `_CROSS_STRATEGY_GUARD_EXCLUDED` (fired-direction
latch, same reasoning as ORB/ATRBreakout — a real bug the full-suite run
caught and fixed). Full backend suite: 2226/2226 pass, ruff/mypy clean.

**Design summary** (see `renko_trend.py`'s own docstring for the complete
version): brick size B derived from multi-day higher-timeframe ATR (or a
fixed value, see extension below), brick engine fed 1-minute closes (finest
resolution this backtest archive has — no tick data exists, documented
substitution, not silently assumed), Fib/POB structure from the first 5-min
candle, `confirm_bricks` gate against checkerboard whipsaws, breakout +
pullback entry modes, dual-layer exit (premium stop/target/trail + Fib
38.2%/61.8% structural invalidation). Day-scoped state (resets every
calendar day, unlike ORB/ATRBreakout's run-scoped `_fired_directions` — a
deliberate, documented improvement since Renko concepts are inherently daily).

**2026-09-22 extension** (same file, additive, every new param defaults to
the original behaviour byte-for-byte): `brick_size_mode="fixed"` +
`fixed_brick_size_points` (skip ATR, use a fixed point value — skips the
ATR sanity-band check too, since that check exists to catch a bad *derived*
value, not a deliberately chosen one), `brick_source_timeframe_minutes`
(build bricks from a resampled 5/15-min candle series instead of every
1-min close — only updates on real HTF-boundary closes via
`is_htf_boundary_close`), `direction_filter_mode="ema_crossover"` (EMA
decides CE/PE instead of Fib/POB; the separate EMA confirmation gate is
skipped in this mode since it'd be redundant), `exit_on_reversal` +
`reversal_confirm_bricks` (structure_level = the price level at which N
bricks would print against the held direction, computed from the live
`RenkoState`'s own box boundaries at signal-fire time via
`_reversal_structure_level` — exact, not an approximation).

## Bundle / box sync state

Local `backtest_engine/` bundle was **fully re-pinned** to this branch's
commit (was stale since 2026-09-01, broke on a surgical partial sync —
see `backtest_engine/VERSION.txt`'s 2026-09-22 entry for the full story).
`resolve_and_qc.py`'s `SOURCE_MAP` gained `"renko_trend": "alice_index"`.
Box (`144.24.137.112`) has the **first-commit version** of `renko_trend.py`
synced (the sweep launched before the extension commit existed) — sweep #1
doesn't use any of the extension's new params so this is fine; **sweep #2
needs the extended `renko_trend.py` synced to the box before it can run**
(only that one file changed in the extension — see "To launch sweep #2"
below).

**SSH note**: copying the private key into the session scratchpad gets
blocked by the auto-mode classifier ("Unauthorized Persistence"). Using the
key directly from its real path in an `ssh`/`scp` command works fine — no
need to copy it. Key: `D:\Documents\Trading Bot_Oracle\ssh-key-2026-08-03_Pvt Key.key`,
user `ubuntu`, host `144.24.137.112`.

## Sweep #1 — RUNNING, check this first

`RUN_TAG=renko1`, systemd unit `backtest-20260922-200614.service`, launched
2026-09-22 20:06:15 UTC. Config file: `backtest_engine/sweep_configs/renko1_trend_timeframe.txt`
(local) / `/home/ubuntu/backtest_engine/sweep_configs/renko1_trend_timeframe.txt`
(box). 9 configs: htf timeframe {30,20,15,10-min, ATR period scaled to hold
lookback constant} x entry_mode {breakout,pullback} x brick multiplier k
{0.75,1.0,1.5} x confirm_bricks {1,2,3} (not a full cross product — see the
config file's own header for the exact 9 combos and reasoning).

Per-config time observed: config 1 (`renko_htf30_k1_cb2_breakout`) took
**1709s (~28.5min)** at SHARD_COUNT=4. Budget ~2.5-4.5h more for the
remaining 8 (started 20:06 UTC, so expect full completion somewhere around
00:00-01:00 UTC / 05:30-06:30 IST 2026-09-23 -- **check the actual wall
clock when you resume, it may already be done**).

Config 1 result (only one confirmed so far): **33 trades, 60.6% win rate,
+Rs5,716 net PnL, profit factor 2.0**. Promising but needs the standard
robustness checks (IS/OOS split, outlier-trade sensitivity, etc. -- this
codebase's own established 7-8 gate bar, see `backend/scripts/BACKTEST_LEARNINGS.md`'s
"CANONICAL RELIABLE-BACKTEST SETUP" section) before trusting it.

**To check status / pull results**:
```
ssh -i "D:\Documents\Trading Bot_Oracle\ssh-key-2026-08-03_Pvt Key.key" ubuntu@144.24.137.112 \
  "journalctl -u backtest-20260922-200614.service --no-pager | tail -60; pgrep -fa run_backtest.py; \
   ls /home/ubuntu/backtest_engine/backend/data/historical/backtest_reports/s6_renko1/*_current.csv"
```
Each `*_current.csv` is a completed config's merged trade log (columns:
symbol,side,leg,entry_time,entry_price,exit_time,exit_price,exit_reason,
qty_lots,lot_size,pnl,...) -- compute win rate/PnL/profit factor from the
`pnl` column same as this session did (see the wakeup prompt pattern in
this session's own transcript, or just: wins=[p for p in pnls if p>0],
PF=sum(wins)/abs(sum(losses))).

**Once the whole sweep is confirmed complete**: `sudo systemctl start
backtest-reaper.timer` on the box (it was stopped before launch per the
engine's own restrictive rule 13 -- **still stopped as of this hand-off,
needs re-enabling once done**).

## Sweep #2 — BUILT, QC'D, NOT LAUNCHED (per explicit user instruction)

User's follow-up variant, evaluated and implemented as the "2026-09-22
extension" above. Config file: `backtest_engine/sweep_configs/renko2_fixed_ema_reversal.txt`
(local only, not yet on the box). 18 configs: fixed brick size {8.33, 12.5}
x brick-source resolution {1,5,15-min} x reversal-exit width
{2,3,4 boxes}, all with `direction_filter_mode="ema_crossover"`, EMA(30)
computed on the same resolution as the brick engine, TSL fixed at
`trail_activation_fraction=0.5`/`trail_lock_fraction=0.6` (not swept — see
the config file's own header comment for the full reasoning, including the
one real design judgment call: the user described a "target" (2-3 boxes)
and a separate "SL" (3-4 boxes) as two different underlying-level exits,
but `TradeProposal` only has one `structure_level` slot -- resolved by
sweeping the width itself (2/3/4) as one axis rather than guessing a
combined rule).

QC'd locally: `resolve_and_qc.py` reports "QC OK -- 18 configs resolved +
validated" against the real `_build_strategy`.

**To launch sweep #2** (only once the user says go, and only after
analyzing sweep #1):
1. Sync the extended `renko_trend.py` to the box (it currently has the
   pre-extension version):
   ```
   scp -i "D:\...\key" backend/app/modules/strategy_engine/strategies/renko_trend.py \
     ubuntu@144.24.137.112:/tmp/renko_trend.py
   ssh -i "D:\...\key" ubuntu@144.24.137.112 \
     "cp /home/ubuntu/backtest_engine/backend/app/modules/strategy_engine/strategies/renko_trend.py \
         /home/ubuntu/backtest_engine/backend/app/modules/strategy_engine/strategies/renko_trend.py.bak-<ts> && \
      cp /tmp/renko_trend.py /home/ubuntu/backtest_engine/backend/app/modules/strategy_engine/strategies/renko_trend.py"
   ```
   Checksum-verify (md5sum both sides) before trusting it.
2. Scp the sweep config: `backtest_engine/sweep_configs/renko2_fixed_ema_reversal.txt`
   -> `/home/ubuntu/backtest_engine/sweep_configs/renko2_fixed_ema_reversal.txt`.
3. Re-run `resolve_and_qc.py` on the box for real (same pattern as sweep #1's
   launch in this session's own transcript) before trusting it.
4. Confirm sweep #1 fully finished + reaper re-enabled, check `pgrep -fa
   run_backtest.py`/`run_sweep` is empty (never run two sweeps concurrently
   -- restrictive rule 10), stop the reaper again before this launch, check
   free disk / time-of-day (off-hours = SHARD_COUNT=4, market hours =
   SHARD_COUNT=2 per the engine's own restrictive rules 6-7).
5. Launch via the detached launcher, same pattern as sweep #1:
   ```
   sudo /opt/backtest/run_bt.sh /bin/bash -c "cd /home/ubuntu/backtest_engine && \
     RUN_TAG=renko2 SHARD_COUNT=4 backend/scripts/run_sweep_canonical.sh \
     /home/ubuntu/backtest_engine/sweep_configs/renko2_fixed_ema_reversal.txt"
   ```
   (Note the exact invocation shape that worked this session -- cwd must be
   the bundle root, script path relative from there, config path absolute.
   The first launch attempt this session got both wrong and failed
   instantly with exit 127 -- worth not repeating.)
6. Budget ~18 configs x per-config time observed from sweep #1 (or this
   sweep's own config 1, if meaningfully different complexity) -- likely a
   multi-hour run, plan accordingly.

## Standing reminders from this session

- Every command against the A1 box touches the **live trading box** (same
  machine, isolated `btengine` DB/venv) -- the engine's own README
  restrictive rules (in `backtest_engine/README.md`) govern all of this:
  never run two sweeps concurrently, stop the reaper before launching,
  re-enable only after full completion, respect market-hours shard-count
  halving, check disk headroom.
- `wip/renko-trend-strategy` stays a local branch, not merged/pushed --
  matches this repo's standing policy (`project_backtest_local_only_standing_policy_2026_09_04`
  memory) of keeping backtest-only strategy work off `main` until it's
  actually decided for paper/live promotion.
- If picking this up fresh: `git checkout wip/renko-trend-strategy` first
  (this session got accidentally switched back to `main` mid-session by
  an unrelated event -- nothing was lost, just re-checkout if `main` is
  what a fresh session lands on).

## UPDATE 2026-09-23 (evening IST): sweep #1 COMPLETE + analyzed -- no config passes
Finished 00:25 UTC (259 min, 9/9 OK). Reaper timer still stopped (not re-enabled; sweep #2 not launched). 1 lot/trade, ~1 trade/day, n=4-51 per config over ~13 months.
| config | n | net | PF | ex-top2 PF | 1H / 2H PF |
| htf30 k1 cb2 breakout | 33 | +5,716 | 2.00 | 1.48 (+2,717) | 0.99 / 3.85 |
| htf30 k1 cb1 | 39 | +3,323 | 1.27 | 0.98 | 14.6 / 0.52 |
| htf10 k1 cb2 | 51 | +3,322 | 1.19 | 0.86 | 3.46 / 0.69 |
| htf20 k1 cb2 | 44 | +2,846 | 1.23 | 0.93 | 1.71 / 0.92 |
| htf30 k1 cb2 pullback | 12 | +3,102 | 5.15 | 1.99 (+742) | 2.7 / 9.3 (n too small) |
| htf30 k1 cb3 | 23 | -1,579 | 0.70 | 0.25 | |
| htf15 k1 cb2 | 49 | -7,465 | 0.66 | | |
| htf30 k0.75 cb2 | 47 | -9,356 | 0.54 | | |
| htf30 k1.5 cb2 | 4 | -527 | 0 | | (brick too big, ~no signals) |
Findings: best config is a lone spike (neighbours cb1/cb3/htf20/k.75/k1.5 all much worse) and its edge is all in 2H (1H flat); most others are 1H-positive/2H-negative. structure_break = 60-75% of exits with median hold **1 min** (23/23 in best config) -> entries fire right at the Fib/structure level and next bar breaches it; net negative in most configs (-5.6k..-12.9k). Trail exits are the only profit source. Best config's 4 EOD square-offs = -3,936. 13:30+ entries lose in best config. Analysis script: scratchpad an.py (per-config n/win%/PF/ex-top2/IS-OOS/exit mix).
Sweep #2 (18 configs) is NOT a "refine after entry learnings" stage -- it is the user's separate variant (fixed brick, EMA30 crossover direction, reversal exit); it holds entry breakout/cb2 fixed and varies exit width. Only 9 configs (not 6) ran in sweep #1.

## CORRECTION + sweep #2a (2026-09-23 evening IST)
A later session (after the hand-off above) built **`renko2a_entry_pilot.txt`** (6 configs: fixed brick {8.33,12.5,25} x resolution {15,30}, EMA30 crossover, reversal_confirm_bricks=3, cb2, breakout) as the staged "decide entry axes first" step; the full 18-config `renko2_fixed_ema_reversal` grid stays deferred and `renko2b_exit_pilot` is planned after 2a. First 2a run (10:19 UTC) gave 0 trades: EMA30 on 15/30-min was day-scoped and never warmed up -> fixed in `04ead50` (multi-day EMA reference, on wip/renko-trend-strategy), reran 12:47-15:41 UTC (173 min, 6/6 OK). I wrongly told the user 9 configs = sweep #2; the 9 is sweep #1 (by design).
2a results (1 lot, ~50 trades each, net / PF / ex-top2 PF / 1H PF -> 2H PF): b833_r15 +7,594/1.53/0.97/2.87->0.93; b125_r30 +3,366/1.21/0.79/2.59->0.44; b833_r30 +394/1.02/0.63/2.17->0.38; b125_r15 -553/0.98/0.68; b25_r30 -1,912/0.91/0.61; b25_r15 -10,700/0.66/0.50. structure_break 30-40 exits/config, net -4.6k..-17.7k every config; trail (4-6 exits) +11.5k..15.5k. All 6 lose money once top-2 removed; 5/6 have 2H worse than 1H. Nothing beats sweep #1's htf30_k1_cb2 (+5,716, ex-top2 PF 1.48). Analysis script: scratchpad an.py.

## 2026-09-23 night: engine PE fix applied + sweep renko2c smoke LAUNCHED
Engine fix applied to `backtest_engine/backend/scripts/run_backtest.py` (bundle only; gitignored; tracked repo copy at backend/scripts/ NOT touched -- shared tree was on branch qc/2026-09-23-observations with another session's uncommitted edits). Box copy synced + md5-verified (7cbd7166dcd0); box backup `run_backtest.py.bak-<ts>` alongside. Smoke: `sweep_configs/renko2c_smoke.txt` (2 configs: fixed 8.33pt/15min and 12.5pt/30min, EMA30 crossover, `reversal_confirm_bricks=1`, `max_signals_per_direction=3`), RUN_TAG=renko2c, unit `backtest-20260923-172447.service`, started 17:24 UTC, ~30 min/config, results in `backtest_reports/s6_renko2c/`. Reaper timer still stopped (re-enable after series). User decisions: exit = 1 completed reverse brick (flat prints no brick -> no exit); 3 signals/dir/day; exit level currently STATIC (dynamic ratcheting level = follow-up idea, needs new exit support in engine + live); other ideas from user pending, not in smoke. Confounded vs 2a by design (fix + 2 param changes); consider a bug-fix-only control if results are ambiguous.

## 2026-09-23 ~18:10 UTC: renko2c smoke config 1 (b833_r15) result + harness finding
Engine fix VERIFIED (PE structure_break now median hold 19m, min 2m; was 1m for 100%). Config 1: 51 trades, win 29.4%, net -3,078, PF 0.91, ex-top2 PF 0.68; CE n19 +2,870 PF1.25 (2a same entries rev3: +8,094 PF1.68 -> rev=1 cut 2 trail winners: trail 6->4, SB 8->12; half of CE SB exits ran >+20% after exit); PE n32 -5,948 PF0.74 (valid for first time). Entries IDENTICAL to 2a (51/51) => `max_signals_per_direction=3` had ZERO effect. ROOT CAUSE (harness): `ConfirmationFilterStrategy.evaluate` returns None while the run has an OPEN Position (`get_open_position_for_run`), and the backtest never closes Positions in replay (exits reconstructed offline) => max 1 trade per run/day for EVERY strategy in backtests; live allows re-entry. Multi-signal/day needs a harness change (close Position in-replay at reconstructed exit_ts). Also `_reconstruct_exit_legs` (leg exit modes) has NO structure-break and NO time-stop logic. Prior evidence to respect: 2026-09-17 "let it run" ledger entry (BACKTEST_LEARNINGS.md L427): looser trail + pure Supertrend-flip exit were decisively worse on id_ema (n=13, possibly PE-bugged) -> test dynamic Renko exit both with and without premium trail. Plan for renko3 (offline paired exit-replay first, then engine `renko_dynamic_exit` via getattr(strategy_obj) + faithful 'completed reverse brick at source-tf boundary') was delivered to the user; NOT run (user said plan only).

## 2026-09-23 ~19:00 UTC: steps 0+1 DONE (offline replay + dynamic Renko exit built), smoke run of config 1 pending user sign-off
- renko2c COMPLETE (both configs, 58 min). Config 2 (12.5pt/30min): 50 trades, net -8,388, PF 0.79, ex-top2 PF 0.61.
- Step 0: scratchpad `replay.py`/`variants.py` (offline paired exit replay over recorded entries + local option/underlying bars). VALIDATED: reproduces renko2c static-exit exits exactly (exit time, price, reason) on 47/47 trades with data (4 trades after 2026-08-20 have no local underlying/option data).
- Step 1: strategy `reversal_exit_mode="dynamic"` (needs exit_on_reversal + brick_size_mode fixed) -> property `dynamic_reversal_exit_spec` {brick_size,timeframe_minutes,confirm_bricks}; committed `d68badc` on wip/renko-trend-strategy (worktree `C:/Users/drvin/tb-renko-fix`, 7 new unit tests pass, ruff/mypy clean). Engine (bundle `run_backtest.py`): `_renko_boundary_events` + `renko_dynamic_exit` param in `_reconstruct_exit_current` (exit reason string `brick_reversal`, evaluated only on source-tf candle closes, supersedes static structure_level, run counter starts at 0 at entry). Engine function == replay on 47/47 for static n=1, dynamic n=1, n=2, and premium trail/target disabled (trail_activation_fraction=1000, target_pct=9.0). Bundle local files updated; BOX NOT YET SYNCED with dynamic change (box has PE-fix-only run_backtest.py, CRLF). PITFALL: Edit tool converts run_backtest.py LF->CRLF; normalize back to LF before syncing (python replace).
- Replay findings (exploratory, 47 paired entries, all variants ex-top2 PF<1): config1 dyn n=1 stop-only (no premium trail/target) +10.6k PF1.33 BUT ONE trade (NIFTY26071424200PE 2026-07-08, +17.7k, entry 121.75 -> 393.8 held to EOD) is the entire edge (ex it: -7.1k); premium trail+target variants ~ -0.7k; config2 best is n=2 stop-only +6.2k / hold-to-EOD +5.4k, dyn n=1 only +0.4k. Premium stop (25-70%) never binds under brick exit. Entry timing 10:15-11:30 n=26 WR19% net -7.4k (post-hoc, tiny n). 42/47 entries already had brick run >=3 (confirm_bricks=2 is a weak gate on 15-min candles that print several bricks). Conclusion: exit choice reshuffles a tail; entry edge unproven.

## LAUNCHED 18:44 UTC: renko3a (single config, dynamic brick exit) -- unit backtest-20260923-184452.service
Config `sweep_configs/renko3a_dyn_smoke.txt` (renko3a_b833_r15_dyn1): renko2c_b833_r15 entry + reversal_exit_mode=dynamic, reversal_confirm_bricks=1, target_pct=9.0, trail_activation_fraction=1000 (premium trail/target off), stop 0.35, max_signals 1. Box synced+md5 verified (run_backtest.py 8a6c524e153d, renko_trend.py d0a3f24bfc4d; backups `*.bak-<ts>-predyn`). ETA ~19:13 UTC; results `backtest_reports/s6_renko3a/renko3a_b833_r15_dyn1_current.csv`. CHECK: (1) entries == renko2c's 51 (2) exit_reason `brick_reversal` present (3) the 47 data-covered trades match replay `variants.py` 'dyn n=1 stop only' (net ~+10.6k) (4) risk engine didn't reject target 9.0. User wants outcome reviewed before any more configs. Reaper timer still stopped.

## UPDATE ~18:55 UTC: renko3a run FAILED (config bug), relaunched as renko3b
First launch (renko3a, 18:44) died in 90s: `trail_activation_fraction=1000` overflows `signals.trail_activation_fraction` Numeric(6,4) (max <100) -> DataError in every shard. Fixed in config (20.0; unreachable given target 9.0), md5-verified on box, relaunched `RUN_TAG=renko3b` unit `backtest-20260923-185047.service` at 18:50:47 UTC (ETA ~19:19). Results: `backtest_reports/s6_renko3b/renko3a_b833_r15_dyn1_current.csv` (config name still renko3a_b833_r15_dyn1). Shard logs live in `/tmp/s6_logs/<RUN_TAG>/` on the box (NOT the journal) -- read those on any "SHARD FAILURES".
User's next-batch asks (planned, not built): (1) flat exit = exit when a source candle prints no favourable brick (replay: k=1 -14.3k? no: config1 -4.3k / config2 -1.6k; k=2 +1.0k / +0.8k; k=3 -13.5k / +5.9k; noisy) -> `flat_exit_candles` param + engine hook TODO; (2) entry: brick run must be FRESH (2nd brick of a new run) -> `max_entry_run_bricks` param TODO (replica: 153/243 days signal vs 242 now for 8.33/15m, first signal ~10:59 vs 09:59; replica approximate: sigrep.py matches actual entries 27/47 (r15) 42/47 (r30) because harness EMA warmup is only 1000 bars). Efficiency: entries are exit-independent -> only ENTRY variants need box runs; exit variants are replayed offline (replay.py == engine on 47/47) on each entry set's CSV.

## 2026-09-23 ~19:15 UTC: entry/exit variation code BUILT (not synced to box, not launched); renko3b still running (ETA 19:19)
Committed `9451cd3` on wip/renko-trend-strategy (worktree C:/Users/drvin/tb-renko-fix): `entry_run_rule` any|fresh|fresh_or_cross (+`ema_cross_lookback_candles`, default 1), `ema_candle_position` close|extreme (extreme = CE needs candle LOW > EMA, PE needs candle HIGH < EMA; breakout+ema_crossover only), `flat_exit_candles` (dynamic mode; in the spec). Pure helpers in renko.py (`trend_run_length`, `entry_run_allowed`, `ema_side_ok`). 104 renko tests pass, mutation-checked (fresh/extreme/cross each bite), ruff+mypy clean (also fixed 7 pre-existing mypy errors in the renko integration test helper). Engine (bundle run_backtest.py) `flat_exit` in `_reconstruct_exit_current`; engine==replay 47/47 for flat k=1,2,3. Bundle strategy files updated locally; BOX still has renko3b-era files -- sync only AFTER renko3b finishes (keep pinned during a run).
NOTE for user: current rule is candle CLOSE vs EMA30 -- there is NO EMA9 anywhere in renko_trend (user believed "EMA 9/30").
Draft batch `sweep_configs/renko3c_entry_batch.txt` (6 configs, one-factor-at-a-time from renko3b baseline, all dyn n=1 exit): fresh, freshcross, tf5, tf20 (8.33pt), ema20, extreme(EMA30). ~29 min each (~3h). Exit variants replayed offline per entry set. Constructed OK locally; QC on box (resolve_and_qc) at launch.

## 2026-09-23 19:20 UTC: renko3b RESULT (dynamic 1-brick exit, premium trail/target off, config b833_r15) + OVERNIGHT BATCH LAUNCHED
renko3b: 51 trades (entries identical to renko2c 51/51), exits brick_reversal 48 (-16.9k) + eod_square_off 3 (+22.7k); net +5,804, PF 1.16, WR 27.5%, avgW 3,070 / avgL -1,005; ex-top2 -16,084 (PF 0.57): top2 = +17,683 (2026-07-08 PE runner) and +4,205; CE +3,796 PF1.35, PE +2,009 PF1.08; H1 +175 / H2 +5,629; maxDD 9,295. Engine == replay on all 47 data-covered trades (net 10,588); the 4 uncovered are small PE losses (-4,784). Mechanics all pass; the edge is 3 EOD runners.
LAUNCHED 19:21:28 UTC: `renko3c` 12-config overnight batch (`sweep_configs/renko3c_overnight_batch.txt`), unit `backtest-20260923-192128.service`, 4 shards, ~29 min each -> ETA ~01:10 UTC (06:40 IST), well before market-hours CPU cap at 03:30 UTC. Command chains `sudo systemctl start backtest-reaper.timer` at the end (rule 13) -- verify it is active in the morning. Files synced+md5 verified (run_backtest.py dccbb59ee705, renko_trend.py 8e633e6dcece, renko.py f4c09eda9019). Results `backtest_reports/s6_renko3c/renko3c_<name>_current.csv`; shard logs `/tmp/s6_logs/renko3c/`. MORNING: `cd scratchpad; scp CSVs to renko3c/; python morning_report.py renko3c` (engine result + offline replay of rev n=1/2/3, flat k=1/2/3, hold-to-EOD per config). Configs: fresh, freshcross, extreme, ema20, tf20, tf5, fresh_ext, freshcross_ext, freshcross_ema20, freshcross_lb2, pullback, b625.

## 2026-09-24 (noon IST): renko3c results + renko4a batch READY (not launched)
- **renko3c (12 configs, all OK)**: tf5 (8.33pt bricks on 5-min candles, EMA30 on 5-min) is the only near-robust base: engine +15,369 PF1.66, ex-top-2 -182, CE +11,173 (PF2.37) / PE +4,196, both halves +. b625 (6.25pt/15-min) +11,833; fresh_ext PE-only edge (PE +16.7k, CE -6.8k). fresh/freshcross/pullback/tf20 hurt. `extreme` == renko3b net was a pure coincidence (different trades). ~2/3 of trades never print a favourable brick (median 0); winners run 7-14 bricks/80-150min; brick continuation ~85-90% per brick at every depth (no natural target); fixed brick targets <=8 hurt; wider/tighter reversal and breakeven variants = noise. Only exit idea that helped: NO-PROGRESS exit (exit if no net favourable brick after N source candles: 2 on 15/20-min, 3 on 5-min), +2-5k on 4/4 15-20min configs, small.
- **Entry features (offline, hypotheses, 9 looked at, n~47)**: (1) don't chase: entries already far from the day's open in trade direction do worse (5/6 half-splits); (2) enter after a turn: more direction flips in today's bricks = better (5/6). Weak: 15-min entries before 10:30 negative, 10:30-12:00 best; climax candle range hurts on 15-min. Offline no-EMA estimate: EMA helps by 15-35k on tf5/15m/b625 (not tf20) -- approximate.
- **Code (commit 36d63b4 on wip/renko-trend-strategy, worktree C:/Users/drvin/tb-renko-fix)**: new params `no_progress_exit_candles` (dynamic exit spec key + engine), `allowed_directions` (both/ce/pe), `max_move_from_open_points`, `min_flips_today`, `direction_filter_mode="none"`; helpers `count_direction_flips`, `move_from_open_ok` in renko.py; 70 renko tests pass, mutation-checked, ruff/mypy clean. Engine (`run_backtest.py` bundle, LF) got no-progress exit (`exit_reason=no_progress`); engine==replay parity 47/47 for noprog 2/3/4 (one fresh_ext trade differs only because the replay lacks the 35% stop). Box synced + md5-verified 2026-09-24 (run_backtest.py 0b12d0d2..., renko.py 7970ddf4..., renko_trend.py 8329e16a...); backups `*.bak-20260924-*` on box. Local bundle backup: scratchpad `run_backtest.py.pre-noprog`.
- **Batch ready**: `sweep_configs/renko4a_entry_batch.txt` (12 configs: tf5_np3, tf5_mv40, tf5_mv60, tf5_flip1, tf5_mv50flip1, tf5_noema, tf5_ceonly, tf5_ema15tf, tf5_fextpe, b625_mv50, b625_st1030, b625_flip1), box QC OK (resolve_and_qc). Smoke: `renko4s_smoke.txt` (5 configs; use `EXTRA_BT_ARGS='--from 2026-08-03 --to 2026-08-14'`, SHARD_COUNT=4 off-hours). Plan: start >=15:30 IST (market-hours rule 6/7), smoke first (~10 min), stop reaper timer first (rule 13), launch detached via run_bt.sh, ~30 min/config (~6h). Analysis: `python report4.py <dir> <config file>` in scratchpad (engine + CE/PE + replay rev1/noprog2/noprog3/rev2). tf5_np3 entries must equal renko3c_tf5 entries (end-to-end check of the exit plumbing). Next: pick best entry configs as bases, larger overnight batch of combinations.
- **SCHEDULED 2026-09-24 12:21 IST**: box unit `backtest-20260924-065118.service` runs `~/backtest_engine/chain_renko4a.sh` -- sleeps to 15:31 IST, stops reaper timer, runs SMOKE renko4s (5 cfgs, 2026-08-03..08-14); launches FULL renko4a (12 cfgs) ONLY if smoke clean (5 OK, no failures/tracebacks, np3 trades>=1); restarts reaper at end. Heartbeat: `~/backtest_engine/logs/renko4_chain.heartbeat`; outputs `logs/renko4s_chain_smoke.out`, `logs/renko4a_chain_full.out`, results `backend/data/historical/backtest_reports/s6_renko4a/`. Expected finish ~22:00-22:30 IST. If smoke fails: full batch not launched, reaper restarted (exit 2).
- **09-24 16:00 IST correction**: the smoke's `--from/--to` did NOT shorten runs (each smoke config = full 51-trade run, ~29 min). So renko4s_* (5 cfgs: tf5_np3, mv50flip1, noema, ceonly, fextpe) are FULL results (dirs s6_renko4s); box `renko4a_entry_batch.txt` trimmed to the other 7 (full 12-list kept as `.full12.txt`). Chain: smoke finishes ~17:55 IST, then 7-config renko4a ~21:25 IST. Analyse both dirs with report4.py (use the full12 config file for params: rename renko4s_X -> renko4a_X names differ, so pass pattern per dir).
- **TO TEST (user, 2026-09-24): ONE merged config with per-direction logic** (CE uses its best entry logic, PE uses its own, inside a single config sharing the one-trade/day slot) -- NOT two separate CE-only/PE-only configs (those give a different outcome: ceonly on tf5 = +4,950 vs +11,173 for the CE half of the base run, because a blocked side lets the harness take later, worse signals). Needs new per-direction params (e.g. ce_*/pe_* overrides for timeframe/EMA/entry_run_rule/ema_candle_position/gates) -- note tf5 CE (PF 2.37) vs fresh_ext PE (PF 2.23) currently need DIFFERENT brick timeframes (5-min vs 15-min), so a merged config may need two brick engines (one per direction) -- design + QC first. Candidate seeds: CE = tf5 base; PE = fresh + extreme (whole candle beyond EMA) on 15m/6.25pt.

## 2026-09-24 night: renko4 results + renko5 OVERNIGHT launched (22:25 IST)
- **renko4 (12 cfgs) results**: best `b625_mv50` (6.25pt, 15-min, EMA30@15, move-from-open cap 50pt): engine +21,349 PF1.58 (CE +5.2k / PE +16.1k), ex2 -12.9k; tf5_np3 +16.2k PF1.75 (ex2 +0.6k); tf5_ema15tf +13.9k. Cap HURTS tf5 (mv40 +3.4k, mv60 +10.4k vs base +15.4k). flip1 / start-10:30 / mv50flip1 / fextpe(tf5) / noema all bad or ~0 (noema -215 => EMA worth ~15k on tf5). ceonly +4,950 (< CE half of base 11,173: blocked side -> worse replacement trades).
- **New code (commit 7124c53 on wip/renko-trend-strategy)**: `entry_mode="candle_confirm"` + `entry_confirm_candles` (5-min brick trend + EMA guide + N consecutive rising/falling 1-min closes, fires on any 1-min bar) and `candle_exit_confirm` (N consecutive adverse 1-min closes -> exit `candle_reversal`; engine + replay `bricks.sim(cexit=N)`, parity 47/47). Box synced+md5-verified (run_backtest.py f68ac3d7..., renko_trend.py 9c67026b...); backups `*.bak-20260924-*precexit/precandle`. Short smoke via `--pairs` (5 days) OK for c3_e5 / c3_e15 / tf10 (script `~/backtest_engine/smoke_renko5.sh`; `--pairs` is the only way to shorten a run).
- **renko5 batch** (`sweep_configs/renko5_overnight_batch.txt`, 12 cfgs, ~30 min each, launched 22:25 IST via `chain_renko5.sh`, unit backtest-20260924-165518.service, heartbeat `logs/renko5_chain.heartbeat`, out `logs/renko5_chain_full.out`, results `s6_renko5/`): c3_e5, c3_e15 (two-timeframe, 3 confirm candles, candle exit 3), b625_mv40/mv60/mv50ext/mv50fresh/mv50ema20, c5_e5, b500_mv50, b833_mv50, c3_e5_mv60, b625_tf10_mv50. Expected end ~04:30 IST; reaper timer stopped until then (chain restarts it). Analysis: `report4.py` (+ replay exit variants incl. cexit).

## 2026-09-24 23:30 IST: FULL HAND-OFF FILE WRITTEN -- read it first
`C:\Users\drvin\Trading Bot\backtest_engine\RENKO_HANDOFF_2026_09_24.md` (also committed on wip/renko-trend-strategy as docs/ops/renko_trend_handoff_2026_09_24.md). Scripts + result CSVs: `backtest_engine/analysis/renko/`. **TOMORROW (user request): refine with a few configs from SWEEP 1 (renko1/renko2a -- Fib/POB trend reference instead of EMA), mix and match with the learnings (dynamic brick exit, candle exit 5, no-progress exit, move-from-open cap).** Also running overnight: renko5 (12 cfgs, ends ~04:25 IST) then chained renko6 (8 cfgs, ends ~08:10 IST).

**2026-09-25 CAVEAT:** every result in this hand-off (renko1-7, top-5, exit replays) is from the WEEKLY harness = Wednesday-only trades (47/50). First per-day run of the base config: -14.1k / PF 0.90 (236 trades). Re-rank per-day; see [[feedback_backtest_default_harness_per_day_2026_09_25]].
