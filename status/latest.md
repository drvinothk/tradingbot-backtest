# btsync status  2026-10-03T17:01:08Z UTC / 2026-10-03 22:31:08 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 22:31:08 IST / 17:01:08 UTC  load: 1.44 1.88 1.81  free: 9G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 1   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema_chain.heartbeat
2026-10-03 22:31:06 IST fxema: ABORT -- a sweep is running
-- fx1_chain.heartbeat
2026-10-03 22:28:19 IST fx1: reaper timer stopped
2026-10-03 22:28:20 IST fx1: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 039d5d7b
2026-10-03 22:30:05 IST fx1: sweep finished rc=0
2026-10-03 22:30:05 IST fx1: chain finished
-- fx0_chain.heartbeat
2026-10-03 22:26:37 IST fx0: reaper timer stopped
2026-10-03 22:26:38 IST fx0: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 039d5d7b
2026-10-03 22:28:18 IST fx0: sweep finished rc=0
2026-10-03 22:28:18 IST fx0: chain finished
== last 8 s6_status lines:
[2026-10-03T16:58:20Z] [fx1] ==========================================
[2026-10-03T16:58:20Z] [fx1] sweep [fx1] -> data/historical/backtest_reports/s6_fx1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-03T16:58:20Z] [fx1] ==========================================
[2026-10-03T16:58:20Z] [fx1] --- EMA_Convic_Paper_Q5Floor_1p1 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activa
[2026-10-03T17:00:04Z] [fx1] EMA_Convic_Paper_Q5Floor_1p1 OK (104s, 24 trades, 61G free)
[2026-10-03T17:00:04Z] [fx1] ==========================================
[2026-10-03T17:00:04Z] [fx1] sweep [fx1] COMPLETE -> data/historical/backtest_reports/s6_fx1 (1min)
[2026-10-03T17:00:04Z] [fx1] ==========================================
== finished configs (all chains): 523
== md5:
039d5d7b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain fxema_chain.heartbeat ended without a finish line (last: 2026-10-03 22:31:06 IST fxema: ABORT -- a sweep is running)
! fxema_chain.heartbeat: 2026-10-03 22:31:06 IST fxema: ABORT -- a sweep is running
```
