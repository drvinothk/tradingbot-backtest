# btsync status  2026-10-09T17:03:10Z UTC / 2026-10-09 22:33:10 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 22:33:10 IST / 17:03:10 UTC  load: 4.81 3.45 1.64  free: 8G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- qch15_tl3_chain.heartbeat
2026-10-09 22:31:41 IST qch15_tl3: reaper timer stopped
2026-10-09 22:31:42 IST qch15_tl3: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qch15_s40t80_chain.heartbeat
2026-10-09 22:29:55 IST qch15_s40t80: reaper timer stopped
2026-10-09 22:29:57 IST qch15_s40t80: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:31:41 IST qch15_s40t80: sweep finished rc=0
2026-10-09 22:31:41 IST qch15_s40t80: chain finished
-- qch15_s30t50_chain.heartbeat
2026-10-09 22:28:10 IST qch15_s30t50: reaper timer stopped
2026-10-09 22:28:12 IST qch15_s30t50: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:29:55 IST qch15_s30t50: sweep finished rc=0
2026-10-09 22:29:55 IST qch15_s30t50: chain finished
== last 8 s6_status lines:
[2026-10-09T17:01:40Z] [qch15_s40t80] VWAP_FX_h15_s40t80 OK (103s, 5 trades, 54G free)
[2026-10-09T17:01:40Z] [qch15_s40t80] ==========================================
[2026-10-09T17:01:40Z] [qch15_s40t80] sweep [qch15_s40t80] COMPLETE -> data/historical/backtest_reports/s6_qch15_s40t80 (1min)
[2026-10-09T17:01:40Z] [qch15_s40t80] ==========================================
[2026-10-09T17:01:42Z] [qch15_tl3] ==========================================
[2026-10-09T17:01:42Z] [qch15_tl3] sweep [qch15_tl3] -> data/historical/backtest_reports/s6_qch15_tl3 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-09T17:01:42Z] [qch15_tl3] ==========================================
[2026-10-09T17:01:42Z] [qch15_tl3] --- VWAP_FX_h15_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
== finished configs (all chains): 551
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
