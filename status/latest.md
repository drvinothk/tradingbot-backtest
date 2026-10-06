# btsync status  2026-10-06T16:12:52Z UTC / 2026-10-06 21:42:52 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-06 21:42:52 IST / 16:12:52 UTC  load: 0.00 0.00 0.00  free: 8G avail  disk: 58G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema5_chain.heartbeat
2026-10-05 17:48:58 IST fxema5: reaper timer stopped
2026-10-05 17:49:00 IST fxema5: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 20:41:12 IST fxema5: sweep finished rc=0
2026-10-05 20:41:12 IST fxema5: chain finished
2026-10-05 20:41:12 IST fxema5: reaper timer restarted
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
== last 8 s6_status lines:
[2026-10-05T12:19:00Z] [fxema5] ==========================================
[2026-10-05T12:19:00Z] [fxema5] sweep [fxema5] -> data/historical/backtest_reports/s6_fxema5 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-05T12:19:00Z] [fxema5] ==========================================
[2026-10-05T12:19:00Z] [fxema5] --- EMA_FX5_floor110_noatr_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activ
[2026-10-05T15:11:12Z] [fxema5] EMA_FX5_floor110_noatr_t05 OK (10332s, 2442 trades, 59G free)
[2026-10-05T15:11:12Z] [fxema5] ==========================================
[2026-10-05T15:11:12Z] [fxema5] sweep [fxema5] COMPLETE -> data/historical/backtest_reports/s6_fxema5 (172min)
[2026-10-05T15:11:12Z] [fxema5] ==========================================
== finished configs (all chains): 535
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
