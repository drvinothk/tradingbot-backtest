# btsync status  2026-10-10T15:24:04Z UTC / 2026-10-10 20:54:04 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 20:54:04 IST / 15:24:04 UTC  load: 4.73 4.71 4.59  free: 8G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap22_chain.heartbeat
2026-10-10 20:21:33 IST fxvwap22: reaper timer stopped
2026-10-10 20:21:35 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap21_chain.heartbeat
2026-10-10 17:57:36 IST fxvwap21: reaper timer stopped
2026-10-10 17:57:37 IST fxvwap21: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 20:21:33 IST fxvwap21: sweep finished rc=0
2026-10-10 20:21:33 IST fxvwap21: chain finished
-- qcf15_f5_nogate_chain.heartbeat
2026-10-10 17:55:49 IST qcf15_f5_nogate: reaper timer stopped
2026-10-10 17:55:50 IST qcf15_f5_nogate: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:57:35 IST qcf15_f5_nogate: sweep finished rc=0
2026-10-10 17:57:35 IST qcf15_f5_nogate: chain finished
== last 8 s6_status lines:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
[2026-10-10T14:51:33Z] [fxvwap21] ==========================================
[2026-10-10T14:51:33Z] [fxvwap21] sweep [fxvwap21] COMPLETE -> data/historical/backtest_reports/s6_fxvwap21 (143min)
[2026-10-10T14:51:33Z] [fxvwap21] ==========================================
[2026-10-10T14:51:35Z] [fxvwap22] ==========================================
[2026-10-10T14:51:35Z] [fxvwap22] sweep [fxvwap22] -> data/historical/backtest_reports/s6_fxvwap22 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T14:51:35Z] [fxvwap22] ==========================================
[2026-10-10T14:51:35Z] [fxvwap22] --- VWAP_FX_f15_base (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
== finished configs (all chains): 561
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
! 1 Traceback line(s) in current shard logs
```
