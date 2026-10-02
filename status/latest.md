# btsync status  2026-10-02T06:54:53Z UTC / 2026-10-02 12:24:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-02 12:24:53 IST / 06:54:53 UTC  load: 0.00 0.01 0.00  free: 10G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- atr_grid2_chain.heartbeat
2026-10-02 04:43:07 IST atr_grid2: start r36 (EMA_Convic_Paper_ATR_R11)
2026-10-02 07:32:15 IST atr_grid2: r36 done (rc=0)
2026-10-02 07:32:15 IST atr_grid2: start r37 (EMA_Convic_Paper_PDT_B20)
2026-10-02 10:23:00 IST atr_grid2: r37 done (rc=0)
2026-10-02 10:23:00 IST atr_grid2: reaper timer restarted
2026-10-02 10:23:00 IST atr_grid2: chain finished
-- r37_chain.heartbeat
2026-10-02 07:32:15 IST r37: reaper timer stopped
2026-10-02 07:32:17 IST r37: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 10:23:00 IST r37: sweep finished rc=0
2026-10-02 10:23:00 IST r37: chain finished
-- r36_chain.heartbeat
2026-10-02 04:43:07 IST r36: reaper timer stopped
2026-10-02 04:43:09 IST r36: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 07:32:15 IST r36: sweep finished rc=0
2026-10-02 07:32:15 IST r36: chain finished
== last 8 s6_status lines:
[2026-10-02T02:02:17Z] [r37] ==========================================
[2026-10-02T02:02:17Z] [r37] sweep [r37] -> data/historical/backtest_reports/s6_r37 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-02T02:02:17Z] [r37] ==========================================
[2026-10-02T02:02:17Z] [r37] --- EMA_Convic_Paper_PDT_B20 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
[2026-10-02T04:53:00Z] [r37] EMA_Convic_Paper_PDT_B20 OK (10243s, 1591 trades, 61G free)
[2026-10-02T04:53:00Z] [r37] ==========================================
[2026-10-02T04:53:00Z] [r37] sweep [r37] COMPLETE -> data/historical/backtest_reports/s6_r37 (170min)
[2026-10-02T04:53:00Z] [r37] ==========================================
== finished configs (all chains): 519
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
