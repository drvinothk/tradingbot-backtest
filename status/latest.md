# btsync status  2026-10-04T07:03:13Z UTC / 2026-10-04 12:33:13 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-04 12:33:13 IST / 07:03:13 UTC  load: 0.00 0.00 0.00  free: 9G avail  disk: 59G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema_chain.heartbeat
2026-10-03 22:31:06 IST fxema: ABORT -- a sweep is running
2026-10-03 22:32:03 IST fxema: reaper timer stopped
2026-10-03 22:32:04 IST fxema: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 039d5d7b
2026-10-04 10:19:23 IST fxema: sweep finished rc=0
2026-10-04 10:19:23 IST fxema: chain finished
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
[2026-10-03T22:45:13Z] [fxema] EMA_FX_ConvicPaper_t03 OK (10309s, 1806 trades, 61G free)
[2026-10-03T22:45:13Z] [fxema] --- EMA_FX_Base_app (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_fracti
[2026-10-04T01:45:56Z] [fxema] EMA_FX_Base_app OK (10843s, 3963 trades, 61G free)
[2026-10-04T01:45:56Z] [fxema] --- EMA_FX_r39spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_fra
[2026-10-04T04:49:23Z] [fxema] EMA_FX_r39spec_t05 OK (11007s, 2092 trades, 59G free)
[2026-10-04T04:49:23Z] [fxema] ==========================================
[2026-10-04T04:49:23Z] [fxema] sweep [fxema] COMPLETE -> data/historical/backtest_reports/s6_fxema (707min)
[2026-10-04T04:49:23Z] [fxema] ==========================================
== finished configs (all chains): 527
== md5:
039d5d7b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
