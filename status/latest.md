# btsync status  2026-10-04T19:46:03Z UTC / 2026-10-05 01:16:03 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-05 01:16:04 IST / 19:46:04 UTC  load: 4.74 4.74 4.73  free: 8G avail  disk: 59G free
== units:
  backtest-20261004-084754.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./launch_config_run.sh fxema2 sweep_configs/
  backtest-20261004-184613.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_fxema3.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxema2_chain.heartbeat
2026-10-04 14:17:54 IST fxema2: reaper timer stopped
2026-10-04 14:17:56 IST fxema2: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine b3b361d7
-- fxv1_chain.heartbeat
2026-10-04 13:09:58 IST fxv1: reaper timer stopped
2026-10-04 13:09:59 IST fxv1: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:11:05 IST fxv1: sweep finished rc=0
2026-10-04 13:11:05 IST fxv1: chain finished
-- fxv0_chain.heartbeat
2026-10-04 13:08:50 IST fxv0: reaper timer stopped
2026-10-04 13:08:51 IST fxv0: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:09:57 IST fxv0: sweep finished rc=0
2026-10-04 13:09:57 IST fxv0: chain finished
== last 8 s6_status lines:
[2026-10-04T08:47:56Z] [fxema2] ==========================================
[2026-10-04T08:47:56Z] [fxema2] --- EMA_FX2_r22spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
[2026-10-04T11:34:40Z] [fxema2] EMA_FX2_r22spec_t05 OK (10004s, 1157 trades, 60G free)
[2026-10-04T11:34:40Z] [fxema2] --- EMA_FX2_r22spec_t03 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
[2026-10-04T14:20:48Z] [fxema2] EMA_FX2_r22spec_t03 OK (9968s, 1173 trades, 60G free)
[2026-10-04T14:20:48Z] [fxema2] --- EMA_FX2_r36spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
[2026-10-04T17:03:35Z] [fxema2] EMA_FX2_r36spec_t05 OK (9767s, 1019 trades, 59G free)
[2026-10-04T17:03:35Z] [fxema2] --- EMA_FX2_floor14_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
== finished configs (all chains): 530
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9749s ago (>2.5h) while a unit is running -- possible stall
```
