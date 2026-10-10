# btsync status  2026-10-10T00:05:00Z UTC / 2026-10-10 05:35:00 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 05:35:00 IST / 00:05:00 UTC  load: 4.58 4.66 4.75  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap17_chain.heartbeat
2026-10-10 03:43:59 IST fxvwap17: reaper timer stopped
2026-10-10 03:44:01 IST fxvwap17: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap16_chain.heartbeat
2026-10-10 01:09:25 IST fxvwap16: reaper timer stopped
2026-10-10 01:09:27 IST fxvwap16: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 03:43:59 IST fxvwap16: sweep finished rc=0
2026-10-10 03:43:59 IST fxvwap16: chain finished
-- fxvwap15_chain.heartbeat
2026-10-09 22:36:54 IST fxvwap15: reaper timer stopped
2026-10-09 22:36:55 IST fxvwap15: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 01:09:25 IST fxvwap15: sweep finished rc=0
2026-10-10 01:09:25 IST fxvwap15: chain finished
== last 8 s6_status lines:
[2026-10-09T22:13:59Z] [fxvwap16] VWAP_FX_h15_s30t50 OK (9272s, 468 trades, 54G free)
[2026-10-09T22:13:59Z] [fxvwap16] ==========================================
[2026-10-09T22:13:59Z] [fxvwap16] sweep [fxvwap16] COMPLETE -> data/historical/backtest_reports/s6_fxvwap16 (154min)
[2026-10-09T22:13:59Z] [fxvwap16] ==========================================
[2026-10-09T22:14:01Z] [fxvwap17] ==========================================
[2026-10-09T22:14:01Z] [fxvwap17] sweep [fxvwap17] -> data/historical/backtest_reports/s6_fxvwap17 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T22:14:01Z] [fxvwap17] ==========================================
[2026-10-09T22:14:01Z] [fxvwap17] --- VWAP_FX_h15_s40t80 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-09T06:23:08Z] [smokehtf5b] VWAP_FX_htf5 HAD SHARD FAILURES (18s, 0 trades, 55G free)
[2026-10-09T06:23:25Z] [smokehtf15b] *** VWAP_FX_htf15 merge FAILED
[2026-10-09T06:23:26Z] [smokehtf15b] VWAP_FX_htf15 HAD SHARD FAILURES (17s, 0 trades, 55G free)
```
