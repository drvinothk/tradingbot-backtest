# btsync status  2026-09-30T20:10:04Z UTC / 2026-10-01 01:40:04 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 01:40:04 IST / 20:10:04 UTC  load: 3.83 4.44 4.65  free: 9G avail  disk: 62G free
== units:
  backtest-20260930-143356.service loaded active running /bin/bash ./chain_final_select2.sh
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r29_chain.heartbeat
2026-09-30 18:52:52 IST r29: reaper timer stopped
2026-09-30 18:52:54 IST r29: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 18:55:06 IST r29: sweep finished rc=0
2026-09-30 18:55:06 IST r29: chain finished
2026-10-01 01:40:02 IST r29: reaper timer stopped
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
[2026-09-30T17:20:26Z] [r25] ==========================================
[2026-09-30T17:20:26Z] [r25] sweep [r25] -> data/historical/backtest_reports/s6_r25 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T17:20:26Z] [r25] ==========================================
[2026-09-30T17:20:26Z] [r25] --- EMA_Convic_Paper_PDTonly (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
[2026-09-30T20:10:02Z] [r25] EMA_Convic_Paper_PDTonly OK (10176s, 1484 trades, 62G free)
[2026-09-30T20:10:02Z] [r25] ==========================================
[2026-09-30T20:10:02Z] [r25] sweep [r25] COMPLETE -> data/historical/backtest_reports/s6_r25 (169min)
[2026-09-30T20:10:02Z] [r25] ==========================================
== finished configs (all chains): 510
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
