# btsync status  2026-10-01T23:44:00Z UTC / 2026-10-02 05:14:00 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-02 05:14:00 IST / 23:44:00 UTC  load: 4.95 4.87 4.80  free: 8G avail  disk: 60G free
== units:
(none running)
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r36_chain.heartbeat
2026-10-02 04:43:07 IST r36: reaper timer stopped
2026-10-02 04:43:09 IST r36: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- atr_grid2_chain.heartbeat
2026-10-02 01:48:34 IST atr_grid2: reaper timer stopped for the whole chain
2026-10-02 01:48:34 IST atr_grid2: start r35 (EMA_Convic_Paper_ATR_R09)
2026-10-02 04:43:07 IST atr_grid2: r35 done (rc=0)
2026-10-02 04:43:07 IST atr_grid2: start r36 (EMA_Convic_Paper_ATR_R11)
-- r35_chain.heartbeat
2026-10-02 01:48:34 IST r35: reaper timer stopped
2026-10-02 01:48:35 IST r35: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 04:43:07 IST r35: sweep finished rc=0
2026-10-02 04:43:07 IST r35: chain finished
== last 8 s6_status lines:
[2026-10-01T23:13:07Z] [r35] EMA_Convic_Paper_ATR_R09 OK (10472s, 2308 trades, 61G free)
[2026-10-01T23:13:07Z] [r35] ==========================================
[2026-10-01T23:13:07Z] [r35] sweep [r35] COMPLETE -> data/historical/backtest_reports/s6_r35 (174min)
[2026-10-01T23:13:07Z] [r35] ==========================================
[2026-10-01T23:13:09Z] [r36] ==========================================
[2026-10-01T23:13:09Z] [r36] sweep [r36] -> data/historical/backtest_reports/s6_r36 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T23:13:09Z] [r36] ==========================================
[2026-10-01T23:13:09Z] [r36] --- EMA_Convic_Paper_ATR_R11 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 517
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r36_chain.heartbeat ended without a finish line (last: 2026-10-02 04:43:09 IST r36: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain atr_grid2_chain.heartbeat ended without a finish line (last: 2026-10-02 04:43:07 IST atr_grid2: start r36 (EMA_Convic_Paper_ATR_R11))
```
