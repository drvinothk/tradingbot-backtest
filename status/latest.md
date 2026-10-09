# btsync status  2026-10-09T10:01:21Z UTC / 2026-10-09 15:31:21 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 15:31:21 IST / 10:01:21 UTC  load: 1.07 0.35 0.24  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-062701.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qchtf_off_chain.heartbeat
2026-10-09 15:31:02 IST qchtf_off: reaper timer stopped
2026-10-09 15:31:05 IST qchtf_off: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- smokehtf15c_chain.heartbeat
2026-10-09 11:55:53 IST smokehtf15c: reaper timer stopped
2026-10-09 11:55:55 IST smokehtf15c: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
2026-10-09 11:56:26 IST smokehtf15c: sweep finished rc=0
2026-10-09 11:56:26 IST smokehtf15c: chain finished
2026-10-09 11:56:26 IST smokehtf15c: reaper timer restarted
-- smokehtf5c_chain.heartbeat
2026-10-09 11:55:18 IST smokehtf5c: reaper timer stopped
2026-10-09 11:55:20 IST smokehtf5c: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
2026-10-09 11:55:53 IST smokehtf5c: sweep finished rc=0
2026-10-09 11:55:53 IST smokehtf5c: chain finished
2026-10-09 11:55:53 IST smokehtf5c: reaper timer restarted
== last 8 s6_status lines:
[2026-10-09T06:26:26Z] [smokehtf15c] VWAP_FX_htf15 OK (31s, 5 trades, 55G free)
[2026-10-09T06:26:26Z] [smokehtf15c] ==========================================
[2026-10-09T06:26:26Z] [smokehtf15c] sweep [smokehtf15c] COMPLETE -> data/historical/backtest_reports/s6_smokehtf15c (0min)
[2026-10-09T06:26:26Z] [smokehtf15c] ==========================================
[2026-10-09T10:01:05Z] [qchtf_off] ==========================================
[2026-10-09T10:01:05Z] [qchtf_off] sweep [qchtf_off] -> data/historical/backtest_reports/s6_qchtf_off (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-09T10:01:05Z] [qchtf_off] ==========================================
[2026-10-09T10:01:05Z] [qchtf_off] --- VWAP_FX_stack_rr11 (vwap_pullback_conviction, src=futures_proxy) params={}
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
