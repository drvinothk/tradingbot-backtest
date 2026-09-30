# btsync status  2026-09-30T23:07:02Z UTC / 2026-10-01 04:37:02 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 04:37:02 IST / 23:07:02 UTC  load: 4.55 4.68 4.71  free: 7G avail  disk: 62G free
== units:
  backtest-20260930-143356.service loaded active running /bin/bash ./chain_final_select2.sh
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r29_chain.heartbeat
2026-09-30 18:52:52 IST r29: reaper timer stopped
2026-09-30 18:52:54 IST r29: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 18:55:06 IST r29: sweep finished rc=0
2026-09-30 18:55:06 IST r29: chain finished
2026-10-01 01:40:02 IST r29: reaper timer stopped
2026-10-01 01:40:04 IST r29: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select2_chain.heartbeat
2026-09-30 20:03:56 IST final_select2: reaper timer stopped for the whole chain
2026-09-30 20:03:56 IST final_select2: start r24 (EMA_Convic_Paper_ATRonly)
2026-09-30 22:50:24 IST final_select2: r24 done (rc=0)
2026-09-30 22:50:24 IST final_select2: start r25 (EMA_Convic_Paper_PDTonly)
2026-10-01 01:40:02 IST final_select2: r25 done (rc=0)
2026-10-01 01:40:02 IST final_select2: start r29 (EMA_Base_Q5Floor_TSL_RedBar1100)
-- r25_chain.heartbeat
2026-09-30 22:50:24 IST r25: reaper timer stopped
2026-09-30 22:50:26 IST r25: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 01:40:02 IST r25: sweep finished rc=0
2026-10-01 01:40:02 IST r25: chain finished
== last 8 s6_status lines:
[2026-09-30T20:10:02Z] [r25] EMA_Convic_Paper_PDTonly OK (10176s, 1484 trades, 62G free)
[2026-09-30T20:10:02Z] [r25] ==========================================
[2026-09-30T20:10:02Z] [r25] sweep [r25] COMPLETE -> data/historical/backtest_reports/s6_r25 (169min)
[2026-09-30T20:10:02Z] [r25] ==========================================
[2026-09-30T20:10:04Z] [r29] ==========================================
[2026-09-30T20:10:04Z] [r29] sweep [r29] -> data/historical/backtest_reports/s6_r29 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T20:10:04Z] [r29] ==========================================
[2026-09-30T20:10:04Z] [r29] --- EMA_Base_Q5Floor_TSL_RedBar1100 (ema_micro_pullback_conviction, src=combined_2020) params={"min_ema_spread_atr_ratio": 1.042, "trail_activation_fraction": 0.3, "trail_
== finished configs (all chains): 510
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 10619s ago (>2.5h) while a unit is running -- possible stall
```
