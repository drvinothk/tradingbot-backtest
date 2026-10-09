# btsync status  2026-10-09T13:34:23Z UTC / 2026-10-09 19:04:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 19:04:23 IST / 13:34:23 UTC  load: 4.60 4.65 4.67  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-062701.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxvwap14_chain.heartbeat
2026-10-09 18:20:35 IST fxvwap14: reaper timer stopped
2026-10-09 18:20:37 IST fxvwap14: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap13_chain.heartbeat
2026-10-09 15:37:30 IST fxvwap13: reaper timer stopped
2026-10-09 15:37:31 IST fxvwap13: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 18:20:35 IST fxvwap13: sweep finished rc=0
2026-10-09 18:20:35 IST fxvwap13: chain finished
-- qchtf15_chain.heartbeat
2026-10-09 15:35:28 IST qchtf15: reaper timer stopped
2026-10-09 15:35:29 IST qchtf15: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 15:37:27 IST qchtf15: sweep finished rc=0
2026-10-09 15:37:27 IST qchtf15: chain finished
== last 8 s6_status lines:
[2026-10-09T12:50:35Z] [fxvwap13] VWAP_FX_htf5 OK (9784s, 609 trades, 54G free)
[2026-10-09T12:50:35Z] [fxvwap13] ==========================================
[2026-10-09T12:50:35Z] [fxvwap13] sweep [fxvwap13] COMPLETE -> data/historical/backtest_reports/s6_fxvwap13 (163min)
[2026-10-09T12:50:35Z] [fxvwap13] ==========================================
[2026-10-09T12:50:37Z] [fxvwap14] ==========================================
[2026-10-09T12:50:37Z] [fxvwap14] sweep [fxvwap14] -> data/historical/backtest_reports/s6_fxvwap14 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T12:50:37Z] [fxvwap14] ==========================================
[2026-10-09T12:50:37Z] [fxvwap14] --- VWAP_FX_htf15 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "trend_lookback_bars": 4, "max_vwap_crosses_in_lookback": 1,
== finished configs (all chains): 548
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
