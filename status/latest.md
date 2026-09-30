# btsync status  2026-09-30T20:01:52Z UTC / 2026-10-01 01:31:52 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 01:31:52 IST / 20:01:52 UTC  load: 4.63 4.72 4.78  free: 7G avail  disk: 62G free
== units:
  backtest-20260930-143356.service loaded active running /bin/bash ./chain_final_select2.sh
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r25_chain.heartbeat
2026-09-30 22:50:24 IST r25: reaper timer stopped
2026-09-30 22:50:26 IST r25: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select2_chain.heartbeat
2026-09-30 20:03:56 IST final_select2: reaper timer stopped for the whole chain
2026-09-30 20:03:56 IST final_select2: start r24 (EMA_Convic_Paper_ATRonly)
2026-09-30 22:50:24 IST final_select2: r24 done (rc=0)
2026-09-30 22:50:24 IST final_select2: start r25 (EMA_Convic_Paper_PDTonly)
-- r24_chain.heartbeat
2026-09-30 10:46:19 IST r24: reaper timer stopped
2026-09-30 10:46:20 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 20:03:56 IST r24: reaper timer stopped
2026-09-30 20:03:57 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 22:50:24 IST r24: sweep finished rc=0
2026-09-30 22:50:24 IST r24: chain finished
== last 8 s6_status lines:
[2026-09-30T17:20:24Z] [r24] EMA_Convic_Paper_ATRonly OK (9987s, 1539 trades, 62G free)
[2026-09-30T17:20:24Z] [r24] ==========================================
[2026-09-30T17:20:24Z] [r24] sweep [r24] COMPLETE -> data/historical/backtest_reports/s6_r24 (166min)
[2026-09-30T17:20:24Z] [r24] ==========================================
[2026-09-30T17:20:26Z] [r25] ==========================================
[2026-09-30T17:20:26Z] [r25] sweep [r25] -> data/historical/backtest_reports/s6_r25 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T17:20:26Z] [r25] ==========================================
[2026-09-30T17:20:26Z] [r25] --- EMA_Convic_Paper_PDTonly (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 509
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9686s ago (>2.5h) while a unit is running -- possible stall
```
