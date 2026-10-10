# btsync status  2026-10-10T12:16:33Z UTC / 2026-10-10 17:46:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 17:46:34 IST / 12:16:34 UTC  load: 2.66 0.76 0.26  free: 8G avail  disk: 54G free
== units:
  backtest-20261010-121534.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qcf15_f15_log_chain.heartbeat
2026-10-10 17:45:34 IST qcf15_f15_log: reaper timer stopped
2026-10-10 17:45:36 IST qcf15_f15_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap20_chain.heartbeat
2026-10-10 11:26:33 IST fxvwap20: reaper timer stopped
2026-10-10 11:26:35 IST fxvwap20: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 13:58:57 IST fxvwap20: sweep finished rc=0
2026-10-10 13:58:57 IST fxvwap20: chain finished
-- fxvwap19_chain.heartbeat
2026-10-10 08:54:44 IST fxvwap19: reaper timer stopped
2026-10-10 08:54:46 IST fxvwap19: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 11:26:33 IST fxvwap19: sweep finished rc=0
2026-10-10 11:26:33 IST fxvwap19: chain finished
== last 8 s6_status lines:
[2026-10-10T08:28:57Z] [fxvwap20] VWAP_FX_h15_norr OK (9142s, 897 trades, 54G free)
[2026-10-10T08:28:57Z] [fxvwap20] ==========================================
[2026-10-10T08:28:57Z] [fxvwap20] sweep [fxvwap20] COMPLETE -> data/historical/backtest_reports/s6_fxvwap20 (152min)
[2026-10-10T08:28:57Z] [fxvwap20] ==========================================
[2026-10-10T12:15:36Z] [qcf15_f15_log] ==========================================
[2026-10-10T12:15:36Z] [qcf15_f15_log] sweep [qcf15_f15_log] -> data/historical/backtest_reports/s6_qcf15_f15_log (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days
[2026-10-10T12:15:36Z] [qcf15_f15_log] ==========================================
[2026-10-10T12:15:36Z] [qcf15_f15_log] --- VWAP_FX_f15_log (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
