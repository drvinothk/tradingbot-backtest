# btsync status  2026-10-01T17:10:30Z UTC / 2026-10-01 22:40:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 22:40:30 IST / 17:10:30 UTC  load: 4.63 4.70 4.72  free: 7G avail  disk: 60G free
== units:
(none running)
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r33_chain.heartbeat
2026-10-01 20:06:49 IST r33: reaper timer stopped
2026-10-01 20:06:52 IST r33: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- atr_grid1_chain.heartbeat
2026-10-01 13:43:52 IST atr_grid1: reaper timer stopped for the whole chain
2026-10-01 13:43:52 IST atr_grid1: start r31 (EMA_Convic_Paper_ATR_L05)
2026-10-01 17:15:47 IST atr_grid1: r31 done (rc=0)
2026-10-01 17:15:47 IST atr_grid1: start r32 (EMA_Convic_Paper_ATR_L10)
2026-10-01 20:06:49 IST atr_grid1: r32 done (rc=0)
2026-10-01 20:06:49 IST atr_grid1: start r33 (EMA_Convic_Paper_ATR_R08)
-- r32_chain.heartbeat
2026-10-01 17:15:47 IST r32: reaper timer stopped
2026-10-01 17:15:49 IST r32: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 20:06:49 IST r32: sweep finished rc=0
2026-10-01 20:06:49 IST r32: chain finished
== last 8 s6_status lines:
[2026-10-01T14:36:49Z] [r32] EMA_Convic_Paper_ATR_L10 OK (10260s, 1834 trades, 61G free)
[2026-10-01T14:36:49Z] [r32] ==========================================
[2026-10-01T14:36:49Z] [r32] sweep [r32] COMPLETE -> data/historical/backtest_reports/s6_r32 (171min)
[2026-10-01T14:36:49Z] [r32] ==========================================
[2026-10-01T14:36:52Z] [r33] ==========================================
[2026-10-01T14:36:52Z] [r33] sweep [r33] -> data/historical/backtest_reports/s6_r33 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T14:36:52Z] [r33] ==========================================
[2026-10-01T14:36:52Z] [r33] --- EMA_Convic_Paper_ATR_R08 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 514
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r33_chain.heartbeat ended without a finish line (last: 2026-10-01 20:06:52 IST r33: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain atr_grid1_chain.heartbeat ended without a finish line (last: 2026-10-01 20:06:49 IST atr_grid1: start r33 (EMA_Convic_Paper_ATR_R08))
```
