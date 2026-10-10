# btsync status  2026-10-10T12:18:54Z UTC / 2026-10-10 17:48:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:48:54 IST / 12:18:54 UTC  load: 4.68 2.37 0.95  free: 9G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- qcf15_f15_base_chain.heartbeat
2026-10-10 17:47:20 IST qcf15_f15_base: reaper timer stopped
2026-10-10 17:47:22 IST qcf15_f15_base: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qcf15_f15_log_chain.heartbeat
2026-10-10 17:45:34 IST qcf15_f15_log: reaper timer stopped
2026-10-10 17:45:36 IST qcf15_f15_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 17:47:20 IST qcf15_f15_log: sweep finished rc=0
2026-10-10 17:47:20 IST qcf15_f15_log: chain finished
-- fxvwap20_chain.heartbeat
2026-10-10 11:26:33 IST fxvwap20: reaper timer stopped
2026-10-10 11:26:35 IST fxvwap20: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 13:58:57 IST fxvwap20: sweep finished rc=0
2026-10-10 13:58:57 IST fxvwap20: chain finished
== last 8 s6_status lines:
[2026-10-10T12:17:20Z] [qcf15_f15_log] VWAP_FX_f15_log OK (104s, 29 trades, 54G free)
[2026-10-10T12:17:20Z] [qcf15_f15_log] ==========================================
[2026-10-10T12:17:20Z] [qcf15_f15_log] sweep [qcf15_f15_log] COMPLETE -> data/historical/backtest_reports/s6_qcf15_f15_log (1min)
[2026-10-10T12:17:20Z] [qcf15_f15_log] ==========================================
[2026-10-10T12:17:22Z] [qcf15_f15_base] ==========================================
[2026-10-10T12:17:22Z] [qcf15_f15_base] sweep [qcf15_f15_base] -> data/historical/backtest_reports/s6_qcf15_f15_base (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-d
[2026-10-10T12:17:22Z] [qcf15_f15_base] ==========================================
[2026-10-10T12:17:22Z] [qcf15_f15_base] --- VWAP_FX_f15_base (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activatio
== finished configs (all chains): 555
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
