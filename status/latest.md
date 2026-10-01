# btsync status  2026-10-01T10:16:50Z UTC / 2026-10-01 15:46:50 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 15:46:50 IST / 10:16:50 UTC  load: 4.53 4.75 4.58  free: 6G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r31_chain.heartbeat
2026-10-01 13:43:52 IST r31: reaper timer stopped
2026-10-01 13:43:54 IST r31: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- atr_grid1_chain.heartbeat
2026-10-01 13:43:52 IST atr_grid1: reaper timer stopped for the whole chain
2026-10-01 13:43:52 IST atr_grid1: start r31 (EMA_Convic_Paper_ATR_L05)
-- final_select2_chain.heartbeat
2026-10-01 01:40:02 IST final_select2: start r29 (EMA_Base_Q5Floor_TSL_RedBar1100)
2026-10-01 04:39:13 IST final_select2: r29 done (rc=0)
2026-10-01 04:39:13 IST final_select2: start r30 (EMA_Convic_Paper_Q5Floor_RedBar1100)
2026-10-01 07:28:53 IST final_select2: r30 done (rc=0)
2026-10-01 07:28:53 IST final_select2: reaper timer restarted
2026-10-01 07:28:53 IST final_select2: chain finished
== last 8 s6_status lines:
[2026-10-01T01:58:53Z] [r30] EMA_Convic_Paper_Q5Floor_RedBar1100 OK (10179s, 1071 trades, 62G free)
[2026-10-01T01:58:53Z] [r30] ==========================================
[2026-10-01T01:58:53Z] [r30] sweep [r30] COMPLETE -> data/historical/backtest_reports/s6_r30 (169min)
[2026-10-01T01:58:53Z] [r30] ==========================================
[2026-10-01T08:13:54Z] [r31] ==========================================
[2026-10-01T08:13:54Z] [r31] sweep [r31] -> data/historical/backtest_reports/s6_r31 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T08:13:54Z] [r31] ==========================================
[2026-10-01T08:13:54Z] [r31] --- EMA_Convic_Paper_ATR_L05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 512
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r31_chain.heartbeat ended without a finish line (last: 2026-10-01 13:43:54 IST r31: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain atr_grid1_chain.heartbeat ended without a finish line (last: 2026-10-01 13:43:52 IST atr_grid1: start r31 (EMA_Convic_Paper_ATR_L05))
```
