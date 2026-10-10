# btsync status  2026-10-10T13:17:14Z UTC / 2026-10-10 18:47:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 18:47:14 IST / 13:17:14 UTC  load: 5.12 4.81 4.64  free: 7G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- fxvwap21_chain.heartbeat
2026-10-10 17:57:36 IST fxvwap21: reaper timer stopped
2026-10-10 17:57:37 IST fxvwap21: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qcf15_f5_nogate_chain.heartbeat
2026-10-10 17:55:49 IST qcf15_f5_nogate: reaper timer stopped
2026-10-10 17:55:50 IST qcf15_f5_nogate: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:57:35 IST qcf15_f5_nogate: sweep finished rc=0
2026-10-10 17:57:35 IST qcf15_f5_nogate: chain finished
-- qcf15_f15_tol_chain.heartbeat
2026-10-10 17:54:06 IST qcf15_f15_tol: reaper timer stopped
2026-10-10 17:54:07 IST qcf15_f15_tol: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:55:48 IST qcf15_f15_tol: sweep finished rc=0
2026-10-10 17:55:48 IST qcf15_f15_tol: chain finished
== last 8 s6_status lines:
[2026-10-10T12:27:35Z] [qcf15_f5_nogate] VWAP_FX_f5_nogate OK (105s, 25 trades, 54G free)
[2026-10-10T12:27:35Z] [qcf15_f5_nogate] ==========================================
[2026-10-10T12:27:35Z] [qcf15_f5_nogate] sweep [qcf15_f5_nogate] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f5_nogate (1min)
[2026-10-10T12:27:35Z] [qcf15_f5_nogate] ==========================================
[2026-10-10T12:27:37Z] [fxvwap21] ==========================================
[2026-10-10T12:27:37Z] [fxvwap21] sweep [fxvwap21] -> data/historical/backtest_reports/s6_fxvwap21 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T12:27:37Z] [fxvwap21] ==========================================
[2026-10-10T12:27:37Z] [fxvwap21] --- VWAP_FX_f15_log (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
== finished configs (all chains): 561
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
