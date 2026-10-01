# btsync status  2026-10-01T21:19:33Z UTC / 2026-10-02 02:49:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-02 02:49:33 IST / 21:19:33 UTC  load: 4.59 4.63 4.63  free: 8G avail  disk: 60G free
== units:
(none running)
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r35_chain.heartbeat
2026-10-02 01:48:34 IST r35: reaper timer stopped
2026-10-02 01:48:35 IST r35: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- atr_grid2_chain.heartbeat
2026-10-02 01:48:34 IST atr_grid2: reaper timer stopped for the whole chain
2026-10-02 01:48:34 IST atr_grid2: start r35 (EMA_Convic_Paper_ATR_R09)
-- atr_grid1_chain.heartbeat
2026-10-01 20:06:49 IST atr_grid1: start r33 (EMA_Convic_Paper_ATR_R08)
2026-10-01 22:59:24 IST atr_grid1: r33 done (rc=0)
2026-10-01 22:59:24 IST atr_grid1: start r34 (EMA_Convic_Paper_ATR_R12)
2026-10-02 01:43:26 IST atr_grid1: r34 done (rc=0)
2026-10-02 01:43:26 IST atr_grid1: reaper timer restarted
2026-10-02 01:43:26 IST atr_grid1: chain finished
== last 8 s6_status lines:
[2026-10-01T20:13:26Z] [r34] EMA_Convic_Paper_ATR_R12 OK (9840s, 449 trades, 61G free)
[2026-10-01T20:13:26Z] [r34] ==========================================
[2026-10-01T20:13:26Z] [r34] sweep [r34] COMPLETE -> data/historical/backtest_reports/s6_r34 (164min)
[2026-10-01T20:13:26Z] [r34] ==========================================
[2026-10-01T20:18:35Z] [r35] ==========================================
[2026-10-01T20:18:35Z] [r35] sweep [r35] -> data/historical/backtest_reports/s6_r35 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T20:18:35Z] [r35] ==========================================
[2026-10-01T20:18:35Z] [r35] --- EMA_Convic_Paper_ATR_R09 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 516
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r35_chain.heartbeat ended without a finish line (last: 2026-10-02 01:48:35 IST r35: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain atr_grid2_chain.heartbeat ended without a finish line (last: 2026-10-02 01:48:34 IST atr_grid2: start r35 (EMA_Convic_Paper_ATR_R09))
```
