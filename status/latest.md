# btsync status  2026-10-03T22:37:14Z UTC / 2026-10-04 04:07:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-04 04:07:14 IST / 22:37:14 UTC  load: 5.21 4.90 4.84  free: 7G avail  disk: 61G free
== units:
  backtest-20261003-170203.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && BT_DECISION_TIME_CHAIN=1 KEEP_REAPER_STOPPED
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxema_chain.heartbeat
2026-10-03 22:31:06 IST fxema: ABORT -- a sweep is running
2026-10-03 22:32:03 IST fxema: reaper timer stopped
2026-10-03 22:32:04 IST fxema: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 039d5d7b
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
[2026-10-03T17:00:04Z] [fx1] sweep [fx1] COMPLETE -> data/historical/backtest_reports/s6_fx1 (1min)
[2026-10-03T17:00:04Z] [fx1] ==========================================
[2026-10-03T17:02:04Z] [fxema] ==========================================
[2026-10-03T17:02:04Z] [fxema] sweep [fxema] -> data/historical/backtest_reports/s6_fxema (4 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-03T17:02:04Z] [fxema] ==========================================
[2026-10-03T17:02:04Z] [fxema] --- EMA_FX_r28spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_fra
[2026-10-03T19:53:24Z] [fxema] EMA_FX_r28spec_t05 OK (10280s, 1779 trades, 61G free)
[2026-10-03T19:53:24Z] [fxema] --- EMA_FX_ConvicPaper_t03 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 524
== md5:
039d5d7b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9830s ago (>2.5h) while a unit is running -- possible stall
```
