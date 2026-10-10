# btsync status  2026-10-10T12:23:29Z UTC / 2026-10-10 17:53:29 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:53:29 IST / 12:23:29 UTC  load: 4.96 3.77 1.90  free: 9G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qcf15_f15_tl3_chain.heartbeat
2026-10-10 17:52:25 IST qcf15_f15_tl3: reaper timer stopped
2026-10-10 17:52:26 IST qcf15_f15_tl3: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qcf15_f15_run_chain.heartbeat
2026-10-10 17:50:44 IST qcf15_f15_run: reaper timer stopped
2026-10-10 17:50:46 IST qcf15_f15_run: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:52:25 IST qcf15_f15_run: sweep finished rc=0
2026-10-10 17:52:25 IST qcf15_f15_run: chain finished
-- qcf15_f15_s40t80_chain.heartbeat
2026-10-10 17:49:03 IST qcf15_f15_s40t80: reaper timer stopped
2026-10-10 17:49:05 IST qcf15_f15_s40t80: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:50:44 IST qcf15_f15_s40t80: sweep finished rc=0
2026-10-10 17:50:44 IST qcf15_f15_s40t80: chain finished
== last 8 s6_status lines:
[2026-10-10T12:22:25Z] [qcf15_f15_run] VWAP_FX_f15_run OK (99s, 13 trades, 54G free)
[2026-10-10T12:22:25Z] [qcf15_f15_run] ==========================================
[2026-10-10T12:22:25Z] [qcf15_f15_run] sweep [qcf15_f15_run] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f15_run (1min)
[2026-10-10T12:22:25Z] [qcf15_f15_run] ==========================================
[2026-10-10T12:22:26Z] [qcf15_f15_tl3] ==========================================
[2026-10-10T12:22:26Z] [qcf15_f15_tl3] sweep [qcf15_f15_tl3] -> data/historical/backtest_reports/s6_qcf15_f15_tl3 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days
[2026-10-10T12:22:26Z] [qcf15_f15_tl3] ==========================================
[2026-10-10T12:22:26Z] [qcf15_f15_tl3] --- VWAP_FX_f15_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_
== finished configs (all chains): 558
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
