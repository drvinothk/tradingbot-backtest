# PLAN — backtest engine: close Positions in-replay so a strategy can trade more than once a day (`--multi-trade`)

Recorded 2026-09-25 (user request: "long-term, robust fix"). Backtest-only work: touches `backtest_engine/backend/scripts/run_backtest.py`
(bundle, gitignored, deployed to the A1 box by `scp`), nothing under `backend/app/` and nothing on the live trading path.
Status: **plan → plan-QC → implement → QC → deploy (only when the box is idle)** — progress log at the bottom.

## 1. Problem and root cause (evidence, not assumption)

Every backtest so far can enter at most **one trade per run** (per-day harness: one per day; weekly harness: one per expiry week).

| link in the chain | where | effect |
|---|---|---|
| Risk approves → `submit_signal` auto-dispatches (paper) | `risk_engine/service.py`, `execution_engine/paper/service.py::dispatch_trade_intent` | a real `Position` row, status OPEN, is created |
| Exits are reconstructed **offline, after** the whole replay | `run_backtest.py::_run_single_backtest` (post-loop) → `_reconstruct_exit_current` | the `Position` is never closed during the replay |
| Every `ConfirmationFilterStrategy` (ORB, VWAP, EMA, OI, Liquidity-Sweep, Renko) returns `None` while the run has an open position | `strategy_engine/common_rules.py::ConfirmationFilterStrategy.evaluate` → `get_open_position_for_run` | after the first trade `check_setup` is never reached again |

Not the cause: risk limits (`max_concurrent_positions=10`, `max_trades_per_day=100`, permissive caps; a real run reports `risk-rejected: 0`).
Confirmed on the box: a per-day renko run logs `1 signal(s), 1 risk-approved, 0 rejected` per day. The 2026-09-23 renko2c note reached the same
root cause ("Multi-signal/day needs a harness change (close Position in-replay at reconstructed exit_ts)") — this plan is that change.

Consequences today: only the first signal of each day is tested (a biased sample — usually the 09:30-10:15 setup), strategy config knobs that only matter
for a second trade (`max_signals_per_direction>1`, EMA `max_trades`, ORB CE-then-PE, re-entry after a stop-out) have **zero effect** in any backtest, and
results do not describe live/paper behaviour, where re-entry is normal.

## 2. Chosen design — "reconstruct at signal time, close in the replay clock" (why this, not an in-loop exit engine)

Rejected: re-implementing the exit logic inside the replay loop (bar-by-bar stop/target/structure/trail/renko-dynamic/candle/no-progress...). That is a
second ~400-line copy of `_reconstruct_exit_current` that would drift from it. Chosen: **reuse the one exit function, call it earlier**.

1. When a signal is risk-approved and dispatched at replay bar *t* (`simulated_time = t+60s`), immediately run `_reconstruct_exit_current` for that
   `TradeIntent` (all its inputs — option bars, underlying series, diagnostics — are preloaded; nothing in it depends on later signals, because at most one
   position is open at a time). This yields the **final `ReconstructedTrade`** (exit time/price/reason/pnl **and** every diagnostic column). It is stored and
   used for the report/CSV instead of re-reconstructing post-hoc → one reconstruction per trade, so "probe vs final" divergence is impossible by construction.
   `atr_series` (diagnostic-only, feeds `atr_exit`) is computed by a deterministic pre-pass over `all_bars` (identical values to the in-loop series).
2. Register `(exit_time, position)` in a pending list. At the top of every later replay cycle (before `run_cycle`), close every pending position whose
   `exit_time <= bar.ts` (+ optional `--reentry-lag-bars N`). `bar.ts <= exit bar` means the exit bar has completed by that cycle's `simulated_time`
   (= bar.ts+60s), i.e. exactly the information a live strategy has when its bar-close evaluation runs. No look-ahead: the strategy only ever sees
   "position still open / now closed", never the future price path.
3. Closing uses production's own `close_position_from_external_fill(db, session, position, TradeFill(exit price, qty, ts=exit_time), exit_reason)`
   (synthetic FILLED closing `Order`, `_finalize_position_close` → `TradeOutcome`, `StopPlan`/`TrailPlan` status, audit event) — the sanctioned "close with an
   externally-known fill" path, so every DB-visible effect is the production one; afterwards `Position.closed_at`, `TradeOutcome.closed_at`, closing
   `Order.updated_at` are corrected to the simulated exit time (same post-hoc correction idea as the existing `_correct_timestamps`), and the execution
   mock's in-memory position book is netted back down (so its margin figure stays honest).
4. **Simulated clock for the risk service.** `risk_engine.service._reentry_cooldown_locked` (production, universal, *all* strategies: block a re-entry on the
   same contract within 5 min of an exit at price ≤ the new entry) reads `_utcnow()` (wall clock). A replay runs in seconds of wall time over historical days,
   so left alone it would either never fire or fire against every later signal. In `--multi-trade` mode `risk_engine.service._utcnow` is patched (module
   attribute, same technique as the existing `_runner_module.is_within_market_hours` patch) to return the current replay `simulated_time`. Result: the cooldown
   behaves in backtest exactly as in production. `--no-reentry-cooldown` (sets `_REENTRY_COOLDOWN = 0`) gives the "pure signal, no cooldown" comparison.
5. Strategies' own state (`_fired_directions`, `trades_fired_count`, `_signals_by_direction`, day-scoped Renko state) is untouched → each strategy's configured
   per-day/per-direction caps become the effective governor, as in live.

## 3. Flags and defaults (nothing changes unless asked)

| flag | default | meaning |
|---|---|---|
| `--multi-trade` | **off** | enable §2. Off ⇒ the new code is never executed ⇒ output byte-identical to today (proved by md5 of CSVs, §6). |
| `--reentry-lag-bars N` | 0 | release a closed position only N bars after its exit bar (conservative sensitivity test; 0 = live-timing) |
| `--no-reentry-cooldown` | off | disable production's 5-min same-contract cooldown for a pure-signal comparison |
| `MULTI_TRADE=1` (env, `run_sweep_perday.sh`) | off | appends `--multi-trade` to every shard invocation. Making it the default of `run_sweep_default.sh` is a **separate, explicit decision** after validation. |

Guard rails (fail loudly, `SystemExit`): `--multi-trade` requires `--exit-mode current` only (one mode drives the replay clock; the leg / legacy modes have
different exit times and cannot share a replay) and requires single-day runs (`--pairs` / `--dates`; strategy latches such as ORB `_fired_directions` and EMA
`trades_fired_count` do not reset daily inside a multi-day `--all-expiries` run, so multi-trade there would silently distort per-day caps).

## 4. Blast analysis

| area | impact | mitigation / proof |
|---|---|---|
| **Sweeps running right now on the A1 box (night2 chain, ends ≤ 08:20 IST 09-26)** | Python loads the file once per process, so a *running* shard is unaffected — **but every later config in the chain starts fresh `python scripts/run_backtest.py` processes** and would load whatever is on disk. An in-place edit would silently mix two engines inside one sweep (violates README rule 4 "one pin per series"). | Develop in a separate file (`run_backtest_mt_dev.py`, never imported by any launcher). **Do not touch the box until the chain is finished** (`systemctl` shows no `backtest-*` run, `night2_chain.heartbeat` says finished). Flag is default-off, so even an early copy would be behaviour-identical — but we still wait. |
| Old results | Every finished result is "first-signal-per-day" (or per-week). They stay valid **as that**. Rows must be labelled; never compared with multi-trade numbers. | README rule 17 gets a companion rule; ledger entry. |
| Tracked repo copy `backend/scripts/run_backtest.py` | already stale (Sep 23, no PE fix) by design. | Left alone; documented. |
| Other `_run_single_backtest` callers (`--all-expiries`, `--dates`, `--pairs` paths in `main()`) | signature gets one keyword-only, defaulted parameter → unchanged for all callers. | Regression run (§6). |
| `merge_backtest_shards.py`, analysis scripts (`analyze_*`, `analysis/renko/*`) | CSV schema is unchanged (same `ReconstructedTrade` fields, one row per trade). More rows per day, sorted by `entry_time`. Scripts that assume ≤1 trade/day (e.g. "per-day dedup", `groupby(date).first()`) would still run but their meaning changes. | Note in README; verify `merge_backtest_shards` handles multiple rows/day. |
| Runtime | `run_cycle` already runs the expensive option-chain refresh every cycle regardless of an open position; `evaluate()` after the first trade was a cheap early-return, now a real `check_setup`. Extra per trade: one probe-free reconstruction (same as before, just earlier) + one close transaction. | Expect ≈ +0-10 %; measure on a 20-day smoke. |
| DB | one more `Order`/`TradeOutcome`/`OrderEvent`/`audit_events` row set per closed trade in a per-run throw-away DB. | negligible. |
| Live trading / `backend/app` / migrations | none. Nothing in `backend/app` is edited; `risk_engine.service._utcnow` is patched **in the backtest process only**. | grep-verified: patch is set only inside `main()`/`_run_single_backtest` under the flag. |
| Production DB / credentials | none (`DB_NAME=btengine`; local test uses `btengine_local_*`). | rule 3 unchanged. |
| Comparability of strategy results | For strategies that can re-signal (ORB CE+PE, EMA, VWAP, OI, Sweep, Renko with `max_signals_per_direction>1`) trade counts rise up to their own caps; the first trade of each day stays identical. | §6 acceptance criteria 2-4. |

## 5. Edge cases (each has a test in §6)

1. **Unresolved trade** (`exit_time is None`: option data ends before an exit is found) → never closed → later signals stay blocked (correct: the position would still be open); counted in the summary.
2. **Exit on the same bar as the next signal's evaluation** (`exit_time == bar.ts`): released at that cycle (live timing); `--reentry-lag-bars 1` shows the sensitivity.
3. **EOD**: exits are ≤ 15:09 (`EOD_CUTOFF`), entries stop at 15:09 by the global trading window → no position crosses a day (single-day runs).
4. **Two positions open at once**: cannot happen for `ConfirmationFilterStrategy`; the pending list is a list anyway and each closes independently.
5. **PENDING_APPROVAL intent without a `Position`** (only if a session were not paper): raise, do not silently skip — invariant broken.
6. **Position has exit legs** (`position_has_exit_legs`): `close_position_from_external_fill` would go through the leg-finalize path and touch a broker → raise (backtest sizes 1 lot ⇒ no legs; if this fires, something upstream changed).
7. **Re-entry cooldown**: closed_at (simulated) vs `_utcnow()` (simulated) — unit-tested both sides of the 5-min boundary and both sides of the price comparison; without the clock patch the test demonstrably fails.
8. **Same-strike lock**: per-strategy, open-position-scoped → clears on close (unit test).
9. **Timezone**: `bar.ts` is IST-aware, `_utcnow()` is UTC-aware; only aware/aware comparisons and SQL timestamptz comparisons are used.
10. **Determinism**: shard split is by `--pairs` (whole days), so multi-trade never crosses a shard; results independent of `SHARD_COUNT`.
11. **`risk_rejected` reasons** now legitimately include `reentry_cooldown_locked`; the summary prints them (already tallied).
12. **Strategy latches consume a rejected signal** (ORB `_fired_directions` set before risk runs) — identical to production; not "fixed".
13. **Clock patch leakage**: `risk_engine.service._utcnow` also stamps `created_at`/`dispatched_at` (later overwritten by `_correct_timestamps`) — harmless; the patch is restored to real time on exit (`try/finally`), so an in-process second run (`--pairs` loop) never sees a stale simulated clock.

## 6. Test plan and acceptance criteria

Unit / DB tests (local Postgres, throw-away `btengine_local_*` databases):
- close helper: Position → CLOSED, TradeOutcome present, simulated timestamps, mock book netted, `get_open_position_for_run` → None, `evaluate()` unblocked;
- risk cooldown with the simulated clock: blocked inside 5 min at price ≥ prior exit, allowed at 5 min+1s, allowed when strictly cheaper, disabled by `--no-reentry-cooldown`;
- guard rails (`--multi-trade` + non-current mode, + multi-day run) exit non-zero with a clear message;
- pre-pass `atr_series` equals the in-loop series (property test on real bars).

Acceptance criteria on real archive data (local bundle has data through 2026-08):
1. **Flag off ⇒ byte-identical**: same 20 `--pairs`, old file vs new file, `md5sum` of merged CSVs equal.
2. **First trade of each day identical** flag-on vs flag-off (row-for-row incl. diagnostics).
3. **No overlap**: within a day, trade *n+1* `entry_time` ≥ trade *n* `exit_time` (+ lag) for every strategy family tested.
4. **Each trade row equals the single-trade reconstruction** of its own intent (spot check with the offline Renko replay `analysis/renko/replay.py`).
5. Trade counts: ORB/EMA/VWAP/OI/Sweep/Renko each show ≥ the flag-off count; days with 2+ trades exist; `reentry_cooldown_locked` appears in the summary where expected.
6. `ruff`-clean file, no change outside the flagged paths (`git diff`-style review of the dev file vs the pinned file).

## 7. Rollout (no surprises for the running box)

1. Dev file + tests locally (this session). 2. Plan-QC and implementation-QC recorded below. 3. Swap `run_backtest.py` locally, backup `.bak-<date>`.
4. **Wait for the night2 chain to finish**; verify box idle; `scp` with md5 check (README rule 15); `VERSION.txt` entry (README rule 4: deliberate re-pin note).
5. Add `MULTI_TRADE` support to `run_sweep_perday.sh`; smoke 5 days on the box; only then decide the default.
6. README + ledger + memory updated; commit docs on a fresh branch off `main` (bundle itself is gitignored).

## 8. Progress log

### 2026-09-26 00:00 IST — plan-QC (before any code) — findings folded into the design above
Verified by reading the code, not assumed:
1. **PE structure-break fix confirmed present** in the bundle engine and on the box (md5 `c115d530…` identical); `structure_favorable` drives both the static and the dynamic Renko structure checks. Records updated (memory).
2. **The blocker is `ConfirmationFilterStrategy.evaluate`'s open-position early-return**, not risk (risk-rejected = 0 in a real per-day renko log). Design keeps every risk rule.
3. **`risk_engine.service._reentry_cooldown_locked` is universal and wall-clock based** — would have silently misbehaved (never or always firing) if the close path had used wall-clock stamps. → simulated-clock patch + `--no-reentry-cooldown` (§2.4). Found by reading, would not have shown up as an error.
4. **Engine exit reasons are not all `ExitReason` members** (`candle_reversal`, `breakeven`, …) and `_finalize_position_close` calls `exit_reason.value` → mapping helper `_domain_exit_reason` (CSV keeps the engine's own string).
5. **The execution mock's position book** (`MockBrokerAdapter._positions`, feeds its `get_margin`) is not touched by an external-fill close → netted down explicitly (10M synthetic margin, so never binding, but kept honest).
6. **Advisory locks are per-database** — `close_position_from_external_fill` takes `LOCK_EXECUTION_SINGLETON`; each replay has its own throw-away DB, so no interaction between shards or with `trading_bot`.
7. **`record_trade_outcome_effects` returns immediately for paper** — no daily-loss-cap / consecutive-loss feedback is introduced (the known "no cross-trade P&L feedback" limitation stays, and matches production paper).
8. **Single reconstruction per trade** (not probe + post-hoc): removes the possibility of the two disagreeing; the ATR pre-pass is asserted equal to the in-loop series every run.
9. Guard rails needed and added: single-day runs only, `--exit-mode current` only.
Open decisions left to the user (defaults chosen, changeable): `--reentry-lag-bars` default 0 (live timing); cooldown ON by default; whether `run_sweep_default.sh` should pass `--multi-trade` by default (NOT done — separate call after validation).

### 2026-09-26 — implementation
Dev copy `backtest_engine/backend/scripts/run_backtest_mt_dev.py` produced from the pinned file by `apply_mt_patch.py` (each replacement asserts its exact match count; pinned file untouched, backup `run_backtest.py.pre-mt-20260925`). ruff (E9,F) clean. Results below.

### 2026-09-26 01:30 IST — implementation QC (local, 6 real days 2026-08-03..10, throw-away DBs, all dropped afterwards)
| check | result |
|---|---|
| flag OFF vs pinned engine (ORB, 6 days) | CSV **byte-identical** (md5 `dd37bb2d…`) |
| first trade of each day, flag ON vs OFF | identical on all columns: ORB 6/6, EMA 6/6 |
| overlaps within a day | 0 (ORB 7 trades, EMA 60 trades) |
| a genuine 2nd trade appears | ORB 2026-08-06: CE stopped 10:03 → PE entered 10:04, PE `structure_break` held 70 min (also live evidence the PE fix works) |
| production cooldown via simulated clock | EMA: 8 `reentry_cooldown_locked` rejections, 60 trades; `--no-reentry-cooldown` 67 trades |
| **mutation check** (clock patch removed) | 67 trades / 0 rejections → the patch is what makes the cooldown real (mutant killed) |
| `--reentry-lag-bars` | lag 1 moved the ORB re-entry 10:04→10:06; lag 3 → no re-entry |
| guard rails (5 cases) | all exit 1 with a clear message |
| ATR pre-pass == in-loop series | asserted every run, never tripped |
| ruff (E9,F) | clean; deliverable md5 `8de4eabc…` == the file that was tested |
Findings: (a) EMA micro-pullback has **no per-day cap of its own** and `max_trades_per_day` is live-scoped in risk, so with multi-trade it fired up to 16×/day — results for uncapped strategies are dominated by that; a backtest-side per-day cap is an open decision. (b) `pnl` of a multi-trade run is not comparable with a first-signal-only run (README rule 18).
Not covered by these runs: VWAP/OI/Sweep/Renko families (same code path; smoke one of each on the box after deploy), and the offline-Renko-replay row check (criterion 4 is met by construction — one shared reconstruction function).

### Deployment status — DONE 2026-09-26 ~01:00 IST
- Box idle at deploy time (the night2 chain had been stopped by the `STOP_PERDAY` flag file, created by someone else at ~00:23 IST; **left in place** — remove `~/backtest_engine/STOP_PERDAY` to let per-day sweeps start again).
- Pre-checks: no `backtest-*` unit running, reaper timer active, `trading-bot` active/`/health` ok; the 7 `backend/app` files the patch imports are md5-identical local == box (pin unchanged).
- Deployed with backups (`~/deploy-bak/*.bak-20260926-multitrade`) and md5 checks: `run_backtest.py` `8de4eabc631dc4c85f7603e0e4e9dbd1`, `run_sweep_perday.sh` `96c6d12206b8726b15acf8c5a3f10344` (adds `MULTI_TRADE=1`, on top of the newer file that already carried the `STOP_PERDAY` pause), plus README / VERSION.txt / BACKTEST_LEARNINGS.md (box == local).
- Box smoke through the capped launcher (`run_bt.sh`, reaper timer stopped/restarted per rule 13, throw-away DBs reaped): ORB, 2 days, flag off vs on → identical first trades, 2 → 3 trades, PE re-entry 2026-08-06 10:04 (`structure_break`, held 70 min) — **row-for-row equal to the local run**.
- Default stays OFF; nothing has been launched with `MULTI_TRADE=1` yet. Still to do before trusting multi-trade sweeps: one VWAP / OI / Liquidity-Sweep / Renko smoke each, and the per-day-cap decision.

### 2026-09-26 ~02:00 IST — DEFAULT DECISION (user) and pending list
User decision: **multi-trade is the normal, unbiased way to backtest and is now the default**; what was run until now (first signal per day / per week) is biased. Only when the user asks for "one trade per day" (quick result) run the per-day first-signal-only variant; **the one-trade-per-week harness is kept completely off**.
- Implemented in the harness scripts (engine unchanged): `run_sweep_perday.sh` adds `--multi-trade` unless `ONE_TRADE_PER_DAY=1` (header log shows `harness=`); `run_sweep_default.sh` rejects `HARNESS=`; `run_sweep.sh` and `backend/scripts/run_sweep_canonical.sh` exit 2. Tested locally (weekly refusals rc=2, default/one-trade flag logic in both modes, `bash -n`). A bare `run_backtest.py` call without the flag is still first-signal-only.
- **~~Deploy PENDING~~ DEPLOYED 2026-09-26 ~11:15 IST** (box idle: `mt1` finished 06:27 IST, `STOP_PERDAY` already removed by its owner; md5-verified box == local for the 4 scripts + README/VERSION/ledger; refusals and `DRY_RUN=1 ./run_sweep_default.sh` re-tested on the box; backups `~/deploy-bak/md-20260926/`). Original note:  the box was running the renko10 `mt1` multi-trade sweep (launched by another session with `MULTI_TRADE=1` on the already-deployed script, `launch_mt1.sh`), and a running `run_sweep_perday.sh` must not be edited in place. Deploy the four scripts + README/VERSION/ledger once no `backtest-*` unit runs; md5-check (box scripts were md5-equal to the local pre-edit backups `*.pre-md-20260926` / `run_sweep_perday.sh.pre-md2-20260926` at 01:10 IST). The running sweep is unaffected either way (`MULTI_TRADE=1` becomes redundant, harmless).
- Side effect: launchers calling `run_sweep_canonical.sh` (`launch_renko7/8/9.sh`, `launch_night2.sh` part B) now refuse; repoint to `run_sweep_default.sh`.
**Pending / to be confirmed**
1. Per-day trade cap for strategies without their own (EMA micro-pullback fired up to 16×/day; `max_trades_per_day` is live-scoped so it does not bind paper/backtest) — decide whether the backtest needs its own cap.
2. Re-run the pre-2026-09-23 PE-side conclusions under the fixed engine (and now multi-trade): renko1/2a, ORB/EMA/VWAP/OI triage, gate grids.
3. Multi-trade smoke on the box for VWAP, OI, Liquidity-Sweep, Renko (only ORB and EMA were exercised).
4. Confirm the defaults `--reentry-lag-bars 0` (live timing) and production cooldown ON.
5. Re-baseline earlier ledger numbers under multi-trade before reusing them as evidence; label every past result's harness.
6. Remove the stale mentions of the weekly harness from older handoff docs (`RENKO_HANDOFF_2026_09_24.md`, ledger 2026-09-25 entry text is historical and stays).

### 2026-09-26 ~11:30 IST — first real multi-trade sweep (renko10 / `mt1`) = independent validation
6 configs × 236 days, 6/6 OK. **The first trade of each day equals the one-trade/day result (parity 236/236 for the base config)** — the engine change does not disturb first-signal behaviour. Trade #2+ (re-entries) lose -62k..-160k in every 5-/15-min-brick candle-exit config (base: 786 trades, first-trade net -14.1k, trade #2+ net -159.8k), so first-signal-only numbers were flattering them; only the ATR-sized `s1_top` was positive (+10.7k gross, cost-adjusted ~0). Full table: bundle `RENKO_HANDOFF_2026_09_24.md` (09-26 11:10). Pending items 1-6 above are unchanged; item 3 (family smokes) is partly covered by this sweep for Renko.
