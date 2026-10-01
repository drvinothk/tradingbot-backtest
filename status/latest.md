# btsync status  2026-10-01T18:00:41Z UTC / 2026-10-01 23:30:41 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-01 23:30:41 IST / 18:00:41 UTC  load: 4.69 4.66 4.66  free: 8G avail  disk: 60G free
== units:
(none running)
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r34_chain.heartbeat
2026-10-01 22:59:24 IST r34: reaper timer stopped
2026-10-01 22:59:26 IST r34: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- atr_grid1_chain.heartbeat
2026-10-01 17:15:47 IST atr_grid1: r31 done (rc=0)
2026-10-01 17:15:47 IST atr_grid1: start r32 (EMA_Convic_Paper_ATR_L10)
2026-10-01 20:06:49 IST atr_grid1: r32 done (rc=0)
2026-10-01 20:06:49 IST atr_grid1: start r33 (EMA_Convic_Paper_ATR_R08)
2026-10-01 22:59:24 IST atr_grid1: r33 done (rc=0)
2026-10-01 22:59:24 IST atr_grid1: start r34 (EMA_Convic_Paper_ATR_R12)
-- r33_chain.heartbeat
2026-10-01 20:06:49 IST r33: reaper timer stopped
2026-10-01 20:06:52 IST r33: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 22:59:24 IST r33: sweep finished rc=0
2026-10-01 22:59:24 IST r33: chain finished
== last 8 s6_status lines:
[2026-10-01T17:29:24Z] [r33] EMA_Convic_Paper_ATR_R08 OK (10352s, 2457 trades, 61G free)
[2026-10-01T17:29:24Z] [r33] ==========================================
[2026-10-01T17:29:24Z] [r33] sweep [r33] COMPLETE -> data/historical/backtest_reports/s6_r33 (172min)
[2026-10-01T17:29:24Z] [r33] ==========================================
[2026-10-01T17:29:26Z] [r34] ==========================================
[2026-10-01T17:29:26Z] [r34] sweep [r34] -> data/historical/backtest_reports/s6_r34 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T17:29:26Z] [r34] ==========================================
[2026-10-01T17:29:26Z] [r34] --- EMA_Convic_Paper_ATR_R12 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 515
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r34_chain.heartbeat ended without a finish line (last: 2026-10-01 22:59:26 IST r34: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain atr_grid1_chain.heartbeat ended without a finish line (last: 2026-10-01 22:59:24 IST atr_grid1: start r34 (EMA_Convic_Paper_ATR_R12))
```
