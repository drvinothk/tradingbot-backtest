# btsync status  2026-10-01T01:46:54Z UTC / 2026-10-01 07:16:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 07:16:54 IST / 01:46:54 UTC  load: 4.58 4.63 4.68  free: 7G avail  disk: 62G free
== units:
  backtest-20260930-143356.service loaded active running /bin/bash ./chain_final_select2.sh
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r30_chain.heartbeat
2026-09-30 18:55:06 IST r30: reaper timer stopped
2026-09-30 18:55:07 IST r30: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 18:57:18 IST r30: sweep finished rc=0
2026-09-30 18:57:18 IST r30: chain finished
2026-10-01 04:39:13 IST r30: reaper timer stopped
2026-10-01 04:39:14 IST r30: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select2_chain.heartbeat
2026-09-30 22:50:24 IST final_select2: r24 done (rc=0)
2026-09-30 22:50:24 IST final_select2: start r25 (EMA_Convic_Paper_PDTonly)
2026-10-01 01:40:02 IST final_select2: r25 done (rc=0)
2026-10-01 01:40:02 IST final_select2: start r29 (EMA_Base_Q5Floor_TSL_RedBar1100)
2026-10-01 04:39:13 IST final_select2: r29 done (rc=0)
2026-10-01 04:39:13 IST final_select2: start r30 (EMA_Convic_Paper_Q5Floor_RedBar1100)
-- r29_chain.heartbeat
2026-09-30 18:55:06 IST r29: sweep finished rc=0
2026-09-30 18:55:06 IST r29: chain finished
2026-10-01 01:40:02 IST r29: reaper timer stopped
2026-10-01 01:40:04 IST r29: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 04:39:13 IST r29: sweep finished rc=0
2026-10-01 04:39:13 IST r29: chain finished
== last 8 s6_status lines:
[2026-09-30T23:09:13Z] [r29] EMA_Base_Q5Floor_TSL_RedBar1100 OK (10749s, 3225 trades, 62G free)
[2026-09-30T23:09:13Z] [r29] ==========================================
[2026-09-30T23:09:13Z] [r29] sweep [r29] COMPLETE -> data/historical/backtest_reports/s6_r29 (179min)
[2026-09-30T23:09:13Z] [r29] ==========================================
[2026-09-30T23:09:14Z] [r30] ==========================================
[2026-09-30T23:09:14Z] [r30] sweep [r30] -> data/historical/backtest_reports/s6_r30 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T23:09:14Z] [r30] ==========================================
[2026-09-30T23:09:14Z] [r30] --- EMA_Convic_Paper_Q5Floor_RedBar1100 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail
== finished configs (all chains): 511
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9460s ago (>2.5h) while a unit is running -- possible stall
```
