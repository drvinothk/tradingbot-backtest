# btsync status  2026-10-10T05:15:31Z UTC / 2026-10-10 10:45:31 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 10:45:32 IST / 05:15:32 UTC  load: 4.52 4.55 4.62  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap19_chain.heartbeat
2026-10-10 08:54:44 IST fxvwap19: reaper timer stopped
2026-10-10 08:54:46 IST fxvwap19: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap18_chain.heartbeat
2026-10-10 06:19:17 IST fxvwap18: reaper timer stopped
2026-10-10 06:19:19 IST fxvwap18: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 08:54:44 IST fxvwap18: sweep finished rc=0
2026-10-10 08:54:44 IST fxvwap18: chain finished
-- fxvwap17_chain.heartbeat
2026-10-10 03:43:59 IST fxvwap17: reaper timer stopped
2026-10-10 03:44:01 IST fxvwap17: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 06:19:17 IST fxvwap17: sweep finished rc=0
2026-10-10 06:19:17 IST fxvwap17: chain finished
== last 8 s6_status lines:
[2026-10-10T03:24:44Z] [fxvwap18] VWAP_FX_h15_tl3 OK (9325s, 461 trades, 54G free)
[2026-10-10T03:24:44Z] [fxvwap18] ==========================================
[2026-10-10T03:24:44Z] [fxvwap18] sweep [fxvwap18] COMPLETE -> data/historical/backtest_reports/s6_fxvwap18 (155min)
[2026-10-10T03:24:44Z] [fxvwap18] ==========================================
[2026-10-10T03:24:46Z] [fxvwap19] ==========================================
[2026-10-10T03:24:46Z] [fxvwap19] sweep [fxvwap19] -> data/historical/backtest_reports/s6_fxvwap19 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T03:24:46Z] [fxvwap19] ==========================================
[2026-10-10T03:24:47Z] [fxvwap19] --- VWAP_FX_h15_tl6 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
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
