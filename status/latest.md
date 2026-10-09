# btsync status  2026-10-09T17:00:53Z UTC / 2026-10-09 22:30:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 22:30:53 IST / 17:00:53 UTC  load: 4.46 2.66 1.13  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qch15_s40t80_chain.heartbeat
2026-10-09 22:29:55 IST qch15_s40t80: reaper timer stopped
2026-10-09 22:29:57 IST qch15_s40t80: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qch15_s30t50_chain.heartbeat
2026-10-09 22:28:10 IST qch15_s30t50: reaper timer stopped
2026-10-09 22:28:12 IST qch15_s30t50: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:29:55 IST qch15_s30t50: sweep finished rc=0
2026-10-09 22:29:55 IST qch15_s30t50: chain finished
-- qch15_c1245_chain.heartbeat
2026-10-09 22:26:23 IST qch15_c1245: reaper timer stopped
2026-10-09 22:26:25 IST qch15_c1245: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:28:10 IST qch15_c1245: sweep finished rc=0
2026-10-09 22:28:10 IST qch15_c1245: chain finished
== last 8 s6_status lines:
[2026-10-09T16:59:55Z] [qch15_s30t50] VWAP_FX_h15_s30t50 OK (103s, 5 trades, 54G free)
[2026-10-09T16:59:55Z] [qch15_s30t50] ==========================================
[2026-10-09T16:59:55Z] [qch15_s30t50] sweep [qch15_s30t50] COMPLETE -> data/historical/backtest_reports/s6_qch15_s30t50 (1min)
[2026-10-09T16:59:55Z] [qch15_s30t50] ==========================================
[2026-10-09T16:59:57Z] [qch15_s40t80] ==========================================
[2026-10-09T16:59:57Z] [qch15_s40t80] sweep [qch15_s40t80] -> data/historical/backtest_reports/s6_qch15_s40t80 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12
[2026-10-09T16:59:57Z] [qch15_s40t80] ==========================================
[2026-10-09T16:59:57Z] [qch15_s40t80] --- VWAP_FX_h15_s40t80 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activatio
== finished configs (all chains): 550
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
