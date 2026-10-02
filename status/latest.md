# btsync status  2026-10-02T11:49:40Z UTC / 2026-10-02 17:19:40 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-02 17:19:40 IST / 11:49:40 UTC  load: 0.09 0.23 0.18  free: 10G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r38_chain.heartbeat
2026-10-02 13:21:20 IST r38: reaper timer stopped
2026-10-02 13:21:21 IST r38: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 16:17:46 IST r38: sweep finished rc=0
2026-10-02 16:17:46 IST r38: chain finished
2026-10-02 16:17:46 IST r38: reaper timer restarted
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
== last 8 s6_status lines:
[2026-10-02T07:51:21Z] [r38] ==========================================
[2026-10-02T07:51:21Z] [r38] sweep [r38] -> data/historical/backtest_reports/s6_r38 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-02T07:51:21Z] [r38] ==========================================
[2026-10-02T07:51:21Z] [r38] --- EMA_Base_Q5Floor_TSL_ATRonly (ema_micro_pullback_conviction, src=combined_2020) params={"min_ema_spread_atr_ratio": 1.042, "trail_activation_fraction": 0.3, "trail_loc
[2026-10-02T10:47:46Z] [r38] EMA_Base_Q5Floor_TSL_ATRonly OK (10585s, 2920 trades, 61G free)
[2026-10-02T10:47:46Z] [r38] ==========================================
[2026-10-02T10:47:46Z] [r38] sweep [r38] COMPLETE -> data/historical/backtest_reports/s6_r38 (176min)
[2026-10-02T10:47:46Z] [r38] ==========================================
== finished configs (all chains): 520
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
