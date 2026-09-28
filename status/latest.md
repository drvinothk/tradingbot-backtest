# btsync status  2026-09-28T16:10:16Z UTC / 2026-09-28 21:40:16 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 21:40:16 IST / 16:10:16 UTC  load: 0.01 0.27 0.89  free: 8G avail  disk: 65G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r17b_chain.heartbeat
2026-09-28 21:32:43 IST r17b: reaper timer stopped
2026-09-28 21:32:45 IST r17b: QC ok; 9 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:33:59 IST r17b: sweep finished rc=0
2026-09-28 21:33:59 IST r17b: chain finished
2026-09-28 21:33:59 IST r17b: reaper timer restarted
-- r17_chain.heartbeat
2026-09-28 17:53:42 IST r17: reaper timer stopped
2026-09-28 17:53:44 IST r17: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:10:59 IST r17: sweep finished rc=0
2026-09-28 21:10:59 IST r17: chain finished
2026-09-28 21:10:59 IST r17: reaper timer restarted
-- r17p_chain.heartbeat
2026-09-28 17:47:08 IST r17p: reaper timer stopped
2026-09-28 17:47:09 IST r17p: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 17:49:08 IST r17p: sweep finished rc=0
2026-09-28 17:49:08 IST r17p: chain finished
2026-09-28 17:49:08 IST r17p: reaper timer restarted
== last 8 s6_status lines:
[2026-09-28T16:02:45Z] [r17b] ==========================================
[2026-09-28T16:02:45Z] [r17b] sweep [r17b] -> data/historical/backtest_reports/s6_r17b (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T16:02:45Z] [r17b] ==========================================
[2026-09-28T16:02:45Z] [r17b] --- EMA_Base (ema_micro_pullback, src=combined_2020) params={"structure_break_atr_multiplier": 0.6, "structure_break_persistence_seconds": 6}
[2026-09-28T16:03:59Z] [r17b] EMA_Base OK (74s, 115 trades, 65G free)
[2026-09-28T16:03:59Z] [r17b] ==========================================
[2026-09-28T16:03:59Z] [r17b] sweep [r17b] COMPLETE -> data/historical/backtest_reports/s6_r17b (1min)
[2026-09-28T16:03:59Z] [r17b] ==========================================
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
