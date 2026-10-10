# btsync status  2026-10-10T12:25:49Z UTC / 2026-10-10 17:55:49 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:55:49 IST / 12:25:49 UTC  load: 4.24 3.94 2.23  free: 10G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- qcf15_f5_nogate_chain.heartbeat
2026-10-10 17:55:49 IST qcf15_f5_nogate: reaper timer stopped
-- qcf15_f15_tol_chain.heartbeat
2026-10-10 17:54:06 IST qcf15_f15_tol: reaper timer stopped
2026-10-10 17:54:07 IST qcf15_f15_tol: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:55:48 IST qcf15_f15_tol: sweep finished rc=0
2026-10-10 17:55:48 IST qcf15_f15_tol: chain finished
-- qcf15_f15_tl3_chain.heartbeat
2026-10-10 17:52:25 IST qcf15_f15_tl3: reaper timer stopped
2026-10-10 17:52:26 IST qcf15_f15_tl3: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:54:06 IST qcf15_f15_tl3: sweep finished rc=0
2026-10-10 17:54:06 IST qcf15_f15_tl3: chain finished
== last 8 s6_status lines:
[2026-10-10T12:24:07Z] [qcf15_f15_tol] ==========================================
[2026-10-10T12:24:07Z] [qcf15_f15_tol] sweep [qcf15_f15_tol] -> data/historical/backtest_reports/s6_qcf15_f15_tol (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days
[2026-10-10T12:24:07Z] [qcf15_f15_tol] ==========================================
[2026-10-10T12:24:07Z] [qcf15_f15_tol] --- VWAP_FX_f15_tol (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_
[2026-10-10T12:25:48Z] [qcf15_f15_tol] VWAP_FX_f15_tol OK (101s, 13 trades, 54G free)
[2026-10-10T12:25:48Z] [qcf15_f15_tol] ==========================================
[2026-10-10T12:25:48Z] [qcf15_f15_tol] sweep [qcf15_f15_tol] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f15_tol (1min)
[2026-10-10T12:25:48Z] [qcf15_f15_tol] ==========================================
== finished configs (all chains): 560
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
