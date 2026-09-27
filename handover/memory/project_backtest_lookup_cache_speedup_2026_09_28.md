---
name: project-backtest-lookup-cache-speedup-2026-09-28
description: "run_backtest.py engine fix (_lookup_nearest_minute id()-caching) - 34% faster, byte-identical verified, deployed (md5 94f7351d). Relevant whenever timing 2020+ data backtests."
metadata:
  type: project
---

Profiled (cProfile) a real 5-day multi-trade slice before evaluating a friend's generic speed-optimization suggestions - found `_lookup_nearest_minute` was 27% of wall time (rebuilt a full O(n) timestamp list, up to ~300k rows, on EVERY call even though the series object never changes within a process). Fixed with `id(series)`-keyed caching; verified byte-identical output (`diff` exit=0) before deploying. Result: 117s->77s on the test slice (34% faster). Deployed, box+local md5 94f7351d (was 587fefca). Backups: box `~/deploy-bak/run_backtest.py.pre-lookupcache-20260928`, local `backend/scripts/run_backtest.py.pre-lookupcache-20260928`.

**Extrapolated new full-year-config time: ~45-50 min (was ~65-70). Full 2020-2026 span (~1640 days) per config: ~5-5.5h (was ~7.5h).**

Other secondary costs found in the same profile, not fixed: CSV parsing/strptime ~16% (unavoidable per-shard), DB commit-per-bar (the `--fast` flag already halves this) ~25% - batching further is a bigger/riskier change, next thing to consider if more speed is needed. Redundant same-week option-CSV reload across days sharing an expiry_dir wasn't isolated in this test (5 distinct weeks tested on purpose) - worth checking if `_load_option_bars` becomes the bottleneck later.

**Why:** user's friend suggested generic data-structure/algorithm refinements before loading newly-purchased 2020+ Nifty options data (would make full-history backtests take far longer without a fix). Chose to profile first rather than guess which suggestions applied.

Full writeup: `backtest_engine/RENKO_HANDOFF_2026_09_24.md` (2026-09-28 entry). Related: [[project_backtest_warmup_flag_and_w12_chain_2026_09_26]], [[project_w13_w14_renko_results_2026_09_27]].
