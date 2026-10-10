# btsync status  2026-10-10T12:21:13Z UTC / 2026-10-10 17:51:13 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:51:13 IST / 12:21:13 UTC  load: 4.78 3.19 1.45  free: 9G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qcf15_f15_run_chain.heartbeat
2026-10-10 17:50:44 IST qcf15_f15_run: reaper timer stopped
2026-10-10 17:50:46 IST qcf15_f15_run: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qcf15_f15_s40t80_chain.heartbeat
2026-10-10 17:49:03 IST qcf15_f15_s40t80: reaper timer stopped
2026-10-10 17:49:05 IST qcf15_f15_s40t80: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:50:44 IST qcf15_f15_s40t80: sweep finished rc=0
2026-10-10 17:50:44 IST qcf15_f15_s40t80: chain finished
-- qcf15_f15_base_chain.heartbeat
2026-10-10 17:47:20 IST qcf15_f15_base: reaper timer stopped
2026-10-10 17:47:22 IST qcf15_f15_base: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:49:03 IST qcf15_f15_base: sweep finished rc=0
2026-10-10 17:49:03 IST qcf15_f15_base: chain finished
== last 8 s6_status lines:
[2026-10-10T12:20:44Z] [qcf15_f15_s40t80] VWAP_FX_f15_s40t80 OK (99s, 14 trades, 54G free)
[2026-10-10T12:20:44Z] [qcf15_f15_s40t80] ==========================================
[2026-10-10T12:20:44Z] [qcf15_f15_s40t80] sweep [qcf15_f15_s40t80] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f15_s40t80 (1min)
[2026-10-10T12:20:44Z] [qcf15_f15_s40t80] ==========================================
[2026-10-10T12:20:46Z] [qcf15_f15_run] ==========================================
[2026-10-10T12:20:46Z] [qcf15_f15_run] sweep [qcf15_f15_run] -> data/historical/backtest_reports/s6_qcf15_f15_run (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days
[2026-10-10T12:20:46Z] [qcf15_f15_run] ==========================================
[2026-10-10T12:20:46Z] [qcf15_f15_run] --- VWAP_FX_f15_run (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_
== finished configs (all chains): 557
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
sort: write failed: 'standard output': Broken pipe
sort: write error
```
