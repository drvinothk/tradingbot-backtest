---
name: feedback-backtest-default-harness-per-day-2026-09-25
description: "STANDING RULE (user, updated 2026-09-26) - every backtest/sweep = per-day MULTI-TRADE (run_sweep_default.sh; normal, unbiased). ONE_TRADE_PER_DAY=1 (first signal only, biased) only when the user explicitly asks. The one-trade-per-expiry-WEEK harness is permanently OFF."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4046aad8-d6b1-4dcd-afdb-32cbcac8b6bb
  modified: 2026-09-25T18:10:47.959Z
---

**Rule.** Default = per-day harness: `sudo /opt/backtest/run_bt.sh /bin/bash -c "cd /home/ubuntu/backtest_engine && RUN_TAG=<tag> SHARD_COUNT=4 ./run_sweep_default.sh sweep_configs/<file>.txt"`. Weekly only with explicit user request (`HARNESS=weekly`, or the raw `run_sweep.sh`/`run_sweep_canonical.sh`, which ARE the weekly harness). Always label which harness a number came from; never compare across harnesses.

**Why.** The weekly `--all-expiries` harness keeps one continuous DB per expiry dir; the first dispatched position never closes in-DB and risk-blocks the rest of the week -> ~50 trades/yr, 47/50 on Wednesday (DTE 6). Renko base config: +29.4k weekly vs -14.1k per-day (236 trades, PF 0.90; Wed +29.2k, every other weekday negative, Tue expiry-day -19.2k). So all renko1..renko7 rankings were Wednesday-only. Per-day parity with weekly on shared days: 50/50 identical.

**How to apply.** New sweeps: use `run_sweep_default.sh` (rebuilds pairs via `setup/build_perday_pairs.py`, runs the canonical QC, then `run_sweep_perday.sh`). Per-day costs ~47 min/config (Renko, SHARD_COUNT=4) vs ~28 weekly - budget for it. Offline replay tools (analysis/renko/replay.py, bricks.py, exitvar*.py) work on per-day CSVs. Docs: backtest_engine/README.md "Run a sweep" + restrictive rule 17, backend/scripts/BACKTEST_LEARNINGS.md 2026-09-25 entry, RENKO_HANDOFF_2026_09_24.md. Old weekly numbers for any strategy (VWAP/ORB/EMA/OI ledger entries) carry the same one-trade-per-week limit - re-run per-day before reusing them as per-day evidence. 25 trading days have no near-week option data (untradable in either harness).

Related: [[project_canonical_sweep_harness_2026_09_05]] (source-resolution + QC gate, still used inside the default entry point), [[project_session_handoff_renko_strategy_2026_09_22]].

**2026-09-26 00:25 PAUSE:** user stopped per-day runs after pd2_mv50 to wait for the other session's `--multi-trade` engine (plan docs/ops/plan_backtest_multi_trade_2026_09_25.md; several trades/day, closer to live). Flag `~/backtest_engine/STOP_PERDAY` blocks new per-day configs; watcher killed; pd3-5 and renko9d NOT run. Resume steps in RENKO_HANDOFF_2026_09_24.md (last section). Multi-trade results are not comparable with 1-trade/day results - label harness.

**2026-09-26 finding:** the 'Wednesday effect' is really DTE 6 = the day AFTER weekly expiry (NIFTY expiry Thu->Tue on 2025-09-01, so Fri before, Wed after). 3-year index-only check (analysis/renko/idx_check.py): DTE6 +12.9 pt (n=157, t 2.0) vs other days -2.2 pt; positive in 6/6 sub-periods; the signal has ~no edge on other days. Per-day option results: base -14.1k, mv50 +3.1k overall, Wed(DTE6) +29.2k/+35.8k. Details in RENKO_HANDOFF_2026_09_24.md.

**2026-09-26 UPDATE (user decision, supersedes the rules above):** default = per-day **multi-trade** (`run_sweep_default.sh` -> `run_sweep_perday.sh` adds `--multi-trade`). `ONE_TRADE_PER_DAY=1` only on explicit "one trade per day" request (quick, biased). **Weekly harness completely off** (`run_sweep.sh`/`run_sweep_canonical.sh` exit 2, `HARNESS=` rejected; do not re-enable). Everything run before 09-26 is first-signal-only or per-week = biased; label it and never compare. **Scripts DEPLOYED to the box 2026-09-26 ~11:15 IST.** Never edit run_sweep_perday.sh / run_backtest.py while a backtest-* unit runs. Pending list: docs/ops/plan_backtest_multi_trade_2026_09_25.md (per-day cap, PE re-runs, family smokes, defaults, re-baseline). See [[project_backtest_multi_trade_engine_2026_09_26]].

**2026-09-26 UPDATE (user decision, made in the multi-trade session): the default is now per-day MULTI-TRADE (`--multi-trade`, MULTI_TRADE=1 until the box scripts are redeployed); the weekly one-trade-per-expiry-week harness is OFF (run_sweep_canonical.sh refuses); first-signal-only per-day (`ONE_TRADE_PER_DAY=1`) only when explicitly asked. This supersedes 'weekly only if user asks' above. The renko10 batch (tag mt1, launched 01:10 IST by the Renko session) is the first multi-trade sweep. Never edit run_sweep_perday.sh/run_sweep_default.sh/run_backtest.py on the box in place while a backtest-* unit runs (use an atomic mv).**

