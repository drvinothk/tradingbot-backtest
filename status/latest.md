# btsync status  2026-10-01T05:32:46Z UTC / 2026-10-01 11:02:46 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 11:02:46 IST / 05:32:46 UTC  load: 0.44 0.37 0.32  free: 8G avail  disk: 62G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- final_select2_chain.heartbeat
2026-10-01 01:40:02 IST final_select2: start r29 (EMA_Base_Q5Floor_TSL_RedBar1100)
2026-10-01 04:39:13 IST final_select2: r29 done (rc=0)
2026-10-01 04:39:13 IST final_select2: start r30 (EMA_Convic_Paper_Q5Floor_RedBar1100)
2026-10-01 07:28:53 IST final_select2: r30 done (rc=0)
2026-10-01 07:28:53 IST final_select2: reaper timer restarted
2026-10-01 07:28:53 IST final_select2: chain finished
-- r30_chain.heartbeat
2026-09-30 18:57:18 IST r30: sweep finished rc=0
2026-09-30 18:57:18 IST r30: chain finished
2026-10-01 04:39:13 IST r30: reaper timer stopped
2026-10-01 04:39:14 IST r30: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 07:28:53 IST r30: sweep finished rc=0
2026-10-01 07:28:53 IST r30: chain finished
-- r29_chain.heartbeat
2026-09-30 18:55:06 IST r29: sweep finished rc=0
2026-09-30 18:55:06 IST r29: chain finished
2026-10-01 01:40:02 IST r29: reaper timer stopped
2026-10-01 01:40:04 IST r29: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 04:39:13 IST r29: sweep finished rc=0
2026-10-01 04:39:13 IST r29: chain finished
== last 8 s6_status lines:
[2026-09-30T23:09:14Z] [r30] ==========================================
[2026-09-30T23:09:14Z] [r30] sweep [r30] -> data/historical/backtest_reports/s6_r30 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T23:09:14Z] [r30] ==========================================
[2026-09-30T23:09:14Z] [r30] --- EMA_Convic_Paper_Q5Floor_RedBar1100 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail
[2026-10-01T01:58:53Z] [r30] EMA_Convic_Paper_Q5Floor_RedBar1100 OK (10179s, 1071 trades, 62G free)
[2026-10-01T01:58:53Z] [r30] ==========================================
[2026-10-01T01:58:53Z] [r30] sweep [r30] COMPLETE -> data/historical/backtest_reports/s6_r30 (169min)
[2026-10-01T01:58:53Z] [r30] ==========================================
== finished configs (all chains): 512
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
