# btsync status  2026-10-01T20:14:30Z UTC / 2026-10-02 01:44:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-02 01:44:30 IST / 20:14:30 UTC  load: 1.19 3.57 4.35  free: 10G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- atr_grid1_chain.heartbeat
2026-10-01 20:06:49 IST atr_grid1: start r33 (EMA_Convic_Paper_ATR_R08)
2026-10-01 22:59:24 IST atr_grid1: r33 done (rc=0)
2026-10-01 22:59:24 IST atr_grid1: start r34 (EMA_Convic_Paper_ATR_R12)
2026-10-02 01:43:26 IST atr_grid1: r34 done (rc=0)
2026-10-02 01:43:26 IST atr_grid1: reaper timer restarted
2026-10-02 01:43:26 IST atr_grid1: chain finished
-- r34_chain.heartbeat
2026-10-01 22:59:24 IST r34: reaper timer stopped
2026-10-01 22:59:26 IST r34: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 01:43:26 IST r34: sweep finished rc=0
2026-10-02 01:43:26 IST r34: chain finished
-- r33_chain.heartbeat
2026-10-01 20:06:49 IST r33: reaper timer stopped
2026-10-01 20:06:52 IST r33: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 22:59:24 IST r33: sweep finished rc=0
2026-10-01 22:59:24 IST r33: chain finished
== last 8 s6_status lines:
[2026-10-01T17:29:26Z] [r34] ==========================================
[2026-10-01T17:29:26Z] [r34] sweep [r34] -> data/historical/backtest_reports/s6_r34 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-01T17:29:26Z] [r34] ==========================================
[2026-10-01T17:29:26Z] [r34] --- EMA_Convic_Paper_ATR_R12 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
[2026-10-01T20:13:26Z] [r34] EMA_Convic_Paper_ATR_R12 OK (9840s, 449 trades, 61G free)
[2026-10-01T20:13:26Z] [r34] ==========================================
[2026-10-01T20:13:26Z] [r34] sweep [r34] COMPLETE -> data/historical/backtest_reports/s6_r34 (164min)
[2026-10-01T20:13:26Z] [r34] ==========================================
== finished configs (all chains): 516
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
