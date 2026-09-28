# btsync status  2026-09-28T12:22:44Z UTC / 2026-09-28 17:52:44 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 17:52:44 IST / 12:22:44 UTC  load: 0.55 0.87 0.51  free: 8G avail  disk: 65G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r17_chain.heartbeat
2026-09-28 17:51:46 IST r17: reaper timer stopped
2026-09-28 17:51:48 IST r17: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 17:52:01 IST r17: sweep finished rc=0
2026-09-28 17:52:01 IST r17: chain finished
2026-09-28 17:52:01 IST r17: reaper timer restarted
-- r17p_chain.heartbeat
2026-09-28 17:47:08 IST r17p: reaper timer stopped
2026-09-28 17:47:09 IST r17p: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 17:49:08 IST r17p: sweep finished rc=0
2026-09-28 17:49:08 IST r17p: chain finished
2026-09-28 17:49:08 IST r17p: reaper timer restarted
-- r16_chain.heartbeat
2026-09-28 02:51:20 IST r16: reaper timer stopped
2026-09-28 02:51:20 IST r16: launching full 2020-2025 sweep: full2020_base (1 config, 1393 day:expiry pairs, 2020-01-01..2025-08-21, source=combined_2020, --extra-warmup-days 12, multi-trade, SHARD_COUNT=4)
2026-09-28 12:34:47 IST r16: sweep finished rc=0
2026-09-28 12:34:47 IST r16: reaper timer restarted
2026-09-28 12:34:47 IST r16: chain finished
== last 8 s6_status lines:
[2026-09-28T12:21:48Z] [r17] sweep [r17] -> data/historical/backtest_reports/s6_r17 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T12:21:48Z] [r17] ==========================================
[2026-09-28T12:21:48Z] [r17] --- EMA_Base (ema_micro_pullback, src=combined_2020) params={"structure_break_atr_multiplier": 0.6, "structure_break_persistence_seconds": 6}
[2026-09-28T12:22:01Z] [r17] *** EMA_Base merge FAILED
[2026-09-28T12:22:01Z] [r17] EMA_Base HAD SHARD FAILURES (13s, 0 trades, 65G free)
[2026-09-28T12:22:01Z] [r17] ==========================================
[2026-09-28T12:22:01Z] [r17] sweep [r17] COMPLETE -> data/historical/backtest_reports/s6_r17 (0min)
[2026-09-28T12:22:01Z] [r17] ==========================================
== finished configs (all chains): 498
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-09-28T12:22:01Z] [r17] *** EMA_Base merge FAILED
[2026-09-28T12:22:01Z] [r17] EMA_Base HAD SHARD FAILURES (13s, 0 trades, 65G free)
```
