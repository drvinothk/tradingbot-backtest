# btsync status  2026-09-28T16:20:20Z UTC / 2026-09-28 21:50:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 21:50:20 IST / 16:20:20 UTC  load: 3.65 2.25 1.38  free: 8G avail  disk: 65G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- p19_chain.heartbeat
2026-09-28 21:48:17 IST p19: reaper timer stopped
2026-09-28 21:48:18 IST p19: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:50:16 IST p19: sweep finished rc=0
2026-09-28 21:50:16 IST p19: chain finished
2026-09-28 21:50:16 IST p19: reaper timer restarted
-- p18_chain.heartbeat
2026-09-28 21:46:17 IST p18: reaper timer stopped
2026-09-28 21:46:18 IST p18: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:48:15 IST p18: sweep finished rc=0
2026-09-28 21:48:15 IST p18: chain finished
2026-09-28 21:48:15 IST p18: reaper timer restarted
-- r17b_chain.heartbeat
2026-09-28 21:32:43 IST r17b: reaper timer stopped
2026-09-28 21:32:45 IST r17b: QC ok; 9 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:33:59 IST r17b: sweep finished rc=0
2026-09-28 21:33:59 IST r17b: chain finished
2026-09-28 21:33:59 IST r17b: reaper timer restarted
== last 8 s6_status lines:
[2026-09-28T16:18:18Z] [p19] ==========================================
[2026-09-28T16:18:18Z] [p19] sweep [p19] -> data/historical/backtest_reports/s6_p19 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T16:18:18Z] [p19] ==========================================
[2026-09-28T16:18:18Z] [p19] --- EMA_PCR_Live_Convic (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buffer_pct"
[2026-09-28T16:20:16Z] [p19] EMA_PCR_Live_Convic OK (118s, 56 trades, 65G free)
[2026-09-28T16:20:16Z] [p19] ==========================================
[2026-09-28T16:20:16Z] [p19] sweep [p19] COMPLETE -> data/historical/backtest_reports/s6_p19 (1min)
[2026-09-28T16:20:16Z] [p19] ==========================================
== finished configs (all chains): 500
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
