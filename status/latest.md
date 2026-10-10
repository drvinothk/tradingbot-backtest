# btsync status  2026-10-10T02:12:03Z UTC / 2026-10-10 07:42:03 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 07:42:03 IST / 02:12:03 UTC  load: 4.76 4.71 4.73  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap18_chain.heartbeat
2026-10-10 06:19:17 IST fxvwap18: reaper timer stopped
2026-10-10 06:19:19 IST fxvwap18: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap17_chain.heartbeat
2026-10-10 03:43:59 IST fxvwap17: reaper timer stopped
2026-10-10 03:44:01 IST fxvwap17: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 06:19:17 IST fxvwap17: sweep finished rc=0
2026-10-10 06:19:17 IST fxvwap17: chain finished
-- fxvwap16_chain.heartbeat
2026-10-10 01:09:25 IST fxvwap16: reaper timer stopped
2026-10-10 01:09:27 IST fxvwap16: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 03:43:59 IST fxvwap16: sweep finished rc=0
2026-10-10 03:43:59 IST fxvwap16: chain finished
== last 8 s6_status lines:
[2026-10-10T00:49:17Z] [fxvwap17] VWAP_FX_h15_s40t80 OK (9316s, 428 trades, 54G free)
[2026-10-10T00:49:17Z] [fxvwap17] ==========================================
[2026-10-10T00:49:17Z] [fxvwap17] sweep [fxvwap17] COMPLETE -> data/historical/backtest_reports/s6_fxvwap17 (155min)
[2026-10-10T00:49:17Z] [fxvwap17] ==========================================
[2026-10-10T00:49:19Z] [fxvwap18] ==========================================
[2026-10-10T00:49:19Z] [fxvwap18] sweep [fxvwap18] -> data/historical/backtest_reports/s6_fxvwap18 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T00:49:19Z] [fxvwap18] ==========================================
[2026-10-10T00:49:19Z] [fxvwap18] --- VWAP_FX_h15_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
