# btsync status  2026-10-08T07:43:29Z UTC / 2026-10-08 13:13:29 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 13:13:29 IST / 07:43:29 UTC  load: 0.22 0.21 0.26  free: 8G avail  disk: 56G free
== units:
  backtest-20261008-074234.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rng_1008.sh"
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema6_chain.heartbeat
2026-10-08 05:31:20 IST fxema6: reaper timer stopped
2026-10-08 05:31:22 IST fxema6: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 08:23:50 IST fxema6: sweep finished rc=0
2026-10-08 08:23:50 IST fxema6: chain finished
-- fxvwap2_chain.heartbeat
2026-10-08 02:31:03 IST fxvwap2: reaper timer stopped
2026-10-08 02:31:04 IST fxvwap2: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 05:31:20 IST fxvwap2: sweep finished rc=0
2026-10-08 05:31:20 IST fxvwap2: chain finished
-- fxorb1_chain.heartbeat
2026-10-07 23:45:22 IST fxorb1: reaper timer stopped
2026-10-07 23:45:23 IST fxorb1: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 02:31:03 IST fxorb1: sweep finished rc=0
2026-10-08 02:31:03 IST fxorb1: chain finished
== last 8 s6_status lines:
[2026-10-08T00:01:22Z] [fxema6] ==========================================
[2026-10-08T00:01:22Z] [fxema6] sweep [fxema6] -> data/historical/backtest_reports/s6_fxema6 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-08T00:01:22Z] [fxema6] ==========================================
[2026-10-08T00:01:22Z] [fxema6] --- EMA_FX_r28_prem40 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_fra
[2026-10-08T02:53:50Z] [fxema6] EMA_FX_r28_prem40 OK (10348s, 1422 trades, 57G free)
[2026-10-08T02:53:50Z] [fxema6] ==========================================
[2026-10-08T02:53:50Z] [fxema6] sweep [fxema6] COMPLETE -> data/historical/backtest_reports/s6_fxema6 (172min)
[2026-10-08T02:53:50Z] [fxema6] ==========================================
== finished configs (all chains): 540
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 17379s ago (>2.5h) while a unit is running -- possible stall
```
