# btsync status  2026-10-09T17:41:20Z UTC / 2026-10-09 23:11:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 23:11:20 IST / 17:41:20 UTC  load: 4.71 4.65 4.41  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap15_chain.heartbeat
2026-10-09 22:36:54 IST fxvwap15: reaper timer stopped
2026-10-09 22:36:55 IST fxvwap15: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qch15_norr_chain.heartbeat
2026-10-09 22:35:11 IST qch15_norr: reaper timer stopped
2026-10-09 22:35:13 IST qch15_norr: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:36:53 IST qch15_norr: sweep finished rc=0
2026-10-09 22:36:53 IST qch15_norr: chain finished
-- qch15_tl6_chain.heartbeat
2026-10-09 22:33:26 IST qch15_tl6: reaper timer stopped
2026-10-09 22:33:27 IST qch15_tl6: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:35:11 IST qch15_tl6: sweep finished rc=0
2026-10-09 22:35:11 IST qch15_tl6: chain finished
== last 8 s6_status lines:
[2026-10-09T17:06:53Z] [qch15_norr] VWAP_FX_h15_norr OK (100s, 13 trades, 54G free)
[2026-10-09T17:06:53Z] [qch15_norr] ==========================================
[2026-10-09T17:06:53Z] [qch15_norr] sweep [qch15_norr] COMPLETE -> data/historical/backtest_reports/s6_qch15_norr (1min)
[2026-10-09T17:06:53Z] [qch15_norr] ==========================================
[2026-10-09T17:06:55Z] [fxvwap15] ==========================================
[2026-10-09T17:06:55Z] [fxvwap15] sweep [fxvwap15] -> data/historical/backtest_reports/s6_fxvwap15 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T17:06:55Z] [fxvwap15] ==========================================
[2026-10-09T17:06:55Z] [fxvwap15] --- VWAP_FX_h15_c1245 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fra
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
