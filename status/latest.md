# btsync status  2026-10-10T12:24:39Z UTC / 2026-10-10 17:54:39 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:54:39 IST / 12:24:39 UTC  load: 4.27 3.81 2.05  free: 9G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qcf15_f15_tol_chain.heartbeat
2026-10-10 17:54:06 IST qcf15_f15_tol: reaper timer stopped
2026-10-10 17:54:07 IST qcf15_f15_tol: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qcf15_f15_tl3_chain.heartbeat
2026-10-10 17:52:25 IST qcf15_f15_tl3: reaper timer stopped
2026-10-10 17:52:26 IST qcf15_f15_tl3: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:54:06 IST qcf15_f15_tl3: sweep finished rc=0
2026-10-10 17:54:06 IST qcf15_f15_tl3: chain finished
-- qcf15_f15_run_chain.heartbeat
2026-10-10 17:50:44 IST qcf15_f15_run: reaper timer stopped
2026-10-10 17:50:46 IST qcf15_f15_run: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:52:25 IST qcf15_f15_run: sweep finished rc=0
2026-10-10 17:52:25 IST qcf15_f15_run: chain finished
== last 8 s6_status lines:
[2026-10-10T12:24:06Z] [qcf15_f15_tl3] VWAP_FX_f15_tl3 OK (100s, 14 trades, 54G free)
[2026-10-10T12:24:06Z] [qcf15_f15_tl3] ==========================================
[2026-10-10T12:24:06Z] [qcf15_f15_tl3] sweep [qcf15_f15_tl3] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f15_tl3 (1min)
[2026-10-10T12:24:06Z] [qcf15_f15_tl3] ==========================================
[2026-10-10T12:24:07Z] [qcf15_f15_tol] ==========================================
[2026-10-10T12:24:07Z] [qcf15_f15_tol] sweep [qcf15_f15_tol] -> data/historical/backtest_reports/s6_qcf15_f15_tol (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days
[2026-10-10T12:24:07Z] [qcf15_f15_tol] ==========================================
[2026-10-10T12:24:07Z] [qcf15_f15_tol] --- VWAP_FX_f15_tol (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_
== finished configs (all chains): 559
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
