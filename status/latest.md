# btsync status  2026-09-30T08:58:13Z UTC / 2026-09-30 14:28:13 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 14:28:13 IST / 08:58:13 UTC  load: 5.87 5.12 4.78  free: 6G avail  disk: 62G free
== units:
  backtest-20260930-061007.service loaded active running /bin/bash ./chain_final_select.sh
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r27_chain.heartbeat
2026-09-30 11:40:07 IST r27: reaper timer stopped
2026-09-30 11:40:08 IST r27: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select_chain.heartbeat
2026-09-30 11:40:07 IST final_select: reaper timer stopped for the whole chain
2026-09-30 11:40:07 IST final_select: start r27 (EMA_Base_Q5Floor_TSL)
-- r24_chain.heartbeat
2026-09-30 10:46:19 IST r24: reaper timer stopped
2026-09-30 10:46:20 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
== last 8 s6_status lines:
[2026-09-30T05:16:20Z] [r24] ==========================================
[2026-09-30T05:16:20Z] [r24] sweep [r24] -> data/historical/backtest_reports/s6_r24 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T05:16:20Z] [r24] ==========================================
[2026-09-30T05:16:20Z] [r24] --- EMA_Convic_Paper_ATRonly (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
[2026-09-30T06:10:08Z] [r27] ==========================================
[2026-09-30T06:10:08Z] [r27] sweep [r27] -> data/historical/backtest_reports/s6_r27 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T06:10:08Z] [r27] ==========================================
[2026-09-30T06:10:08Z] [r27] --- EMA_Base_Q5Floor_TSL (ema_micro_pullback_conviction, src=combined_2020) params={"min_ema_spread_atr_ratio": 1.042, "trail_activation_fraction": 0.3, "trail_lock_fracti
== finished configs (all chains): 504
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 10085s ago (>2.5h) while a unit is running -- possible stall
```
