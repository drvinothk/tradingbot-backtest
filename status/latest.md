# btsync status  2026-10-05T12:05:12Z UTC / 2026-10-05 17:35:12 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-05 17:35:12 IST / 12:05:12 UTC  load: 0.05 0.01 0.00  free: 8G avail  disk: 59G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema4_chain.heartbeat
2026-10-05 06:56:03 IST fxema4: reaper timer stopped
2026-10-05 06:56:05 IST fxema4: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 09:59:55 IST fxema4: sweep finished rc=0
2026-10-05 09:59:55 IST fxema4: chain finished
2026-10-05 09:59:55 IST fxema4: reaper timer restarted
-- fxema3_chain.heartbeat
2026-10-05 01:17:16 IST fxema3: reaper timer stopped
2026-10-05 01:17:18 IST fxema3: QC ok; 1636 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 06:54:33 IST fxema3: sweep finished rc=0
2026-10-05 06:54:33 IST fxema3: chain finished
2026-10-05 06:54:33 IST fxema3: reaper timer restarted
-- fxema2_chain.heartbeat
2026-10-04 14:17:54 IST fxema2: reaper timer stopped
2026-10-04 14:17:56 IST fxema2: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 01:16:11 IST fxema2: sweep finished rc=0
2026-10-05 01:16:11 IST fxema2: chain finished
2026-10-05 01:16:11 IST fxema2: reaper timer restarted
== last 8 s6_status lines:
[2026-10-05T01:26:05Z] [fxema4] ==========================================
[2026-10-05T01:26:05Z] [fxema4] sweep [fxema4] -> data/historical/backtest_reports/s6_fxema4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-05T01:26:05Z] [fxema4] ==========================================
[2026-10-05T01:26:05Z] [fxema4] --- EMA_FX4_floor130_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
[2026-10-05T04:29:54Z] [fxema4] EMA_FX4_floor130_t05 OK (11029s, 935 trades, 59G free)
[2026-10-05T04:29:54Z] [fxema4] ==========================================
[2026-10-05T04:29:54Z] [fxema4] sweep [fxema4] COMPLETE -> data/historical/backtest_reports/s6_fxema4 (183min)
[2026-10-05T04:29:54Z] [fxema4] ==========================================
== finished configs (all chains): 534
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
