# btsync status  2026-10-02T18:51:30Z UTC / 2026-10-03 00:21:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 00:21:30 IST / 18:51:30 UTC  load: 0.04 0.06 0.68  free: 9G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r39_chain.heartbeat
2026-10-02 20:59:10 IST r39: reaper timer stopped
2026-10-02 20:59:12 IST r39: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 23:50:05 IST r39: sweep finished rc=0
2026-10-02 23:50:05 IST r39: chain finished
2026-10-02 23:50:05 IST r39: reaper timer restarted
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
== last 8 s6_status lines:
[2026-10-02T15:29:12Z] [r39] ==========================================
[2026-10-02T15:29:12Z] [r39] sweep [r39] -> data/historical/backtest_reports/s6_r39 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-02T15:29:12Z] [r39] ==========================================
[2026-10-02T15:29:12Z] [r39] --- EMA_Base_Q5Floor_TSL_BothGates (ema_micro_pullback_conviction, src=combined_2020) params={"min_ema_spread_atr_ratio": 1.042, "trail_activation_fraction": 0.3, "trail_l
[2026-10-02T18:20:05Z] [r39] EMA_Base_Q5Floor_TSL_BothGates OK (10253s, 2097 trades, 61G free)
[2026-10-02T18:20:05Z] [r39] ==========================================
[2026-10-02T18:20:05Z] [r39] sweep [r39] COMPLETE -> data/historical/backtest_reports/s6_r39 (170min)
[2026-10-02T18:20:05Z] [r39] ==========================================
== finished configs (all chains): 521
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
