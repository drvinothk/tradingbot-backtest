# btsync status  2026-10-08T00:36:44Z UTC / 2026-10-08 06:06:44 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 06:06:44 IST / 00:36:44 UTC  load: 4.76 4.66 4.69  free: 9G avail  disk: 56G free
== units:
  backtest-20261007-181522.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_fx_1007.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxema6_chain.heartbeat
2026-10-08 05:31:20 IST fxema6: reaper timer stopped
2026-10-08 05:31:22 IST fxema6: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
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
[2026-10-08T00:01:20Z] [fxvwap2] VWAP_FX_nopcr_stack OK (10816s, 5371 trades, 57G free)
[2026-10-08T00:01:20Z] [fxvwap2] ==========================================
[2026-10-08T00:01:20Z] [fxvwap2] sweep [fxvwap2] COMPLETE -> data/historical/backtest_reports/s6_fxvwap2 (180min)
[2026-10-08T00:01:20Z] [fxvwap2] ==========================================
[2026-10-08T00:01:22Z] [fxema6] ==========================================
[2026-10-08T00:01:22Z] [fxema6] sweep [fxema6] -> data/historical/backtest_reports/s6_fxema6 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-08T00:01:22Z] [fxema6] ==========================================
[2026-10-08T00:01:22Z] [fxema6] --- EMA_FX_r28_prem40 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_fra
== finished configs (all chains): 539
== md5:
2d185d39 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
