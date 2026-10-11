# btsync status  2026-10-11T17:11:43Z UTC / 2026-10-11 22:41:43 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 22:41:43 IST / 17:11:43 UTC  load: 0.00 0.15 1.52  free: 10G avail  disk: 52G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxvwap31_chain.heartbeat
2026-10-11 19:55:50 IST fxvwap31: reaper timer stopped
2026-10-11 19:55:51 IST fxvwap31: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 22:23:48 IST fxvwap31: sweep finished rc=0
2026-10-11 22:23:48 IST fxvwap31: chain finished
-- fxvwap30_chain.heartbeat
2026-10-11 17:29:12 IST fxvwap30: reaper timer stopped
2026-10-11 17:29:13 IST fxvwap30: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 19:55:46 IST fxvwap30: sweep finished rc=0
2026-10-11 19:55:46 IST fxvwap30: chain finished
-- fxvwap29_chain.heartbeat
2026-10-11 16:59:36 IST fxvwap29: reaper timer stopped
2026-10-11 16:59:38 IST fxvwap29: QC ok; 314 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 17:29:12 IST fxvwap29: sweep finished rc=0
2026-10-11 17:29:12 IST fxvwap29: chain finished
== last 8 s6_status lines:
[2026-10-11T14:25:51Z] [fxvwap31] ==========================================
[2026-10-11T14:25:51Z] [fxvwap31] sweep [fxvwap31] -> data/historical/backtest_reports/s6_fxvwap31 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T14:25:51Z] [fxvwap31] ==========================================
[2026-10-11T14:25:51Z] [fxvwap31] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activati
[2026-10-11T16:53:48Z] [fxvwap31] VWAP_FX_s15_expatm_p250 OK (8877s, 1819 trades, 52G free)
[2026-10-11T16:53:48Z] [fxvwap31] ==========================================
[2026-10-11T16:53:48Z] [fxvwap31] sweep [fxvwap31] COMPLETE -> data/historical/backtest_reports/s6_fxvwap31 (147min)
[2026-10-11T16:53:48Z] [fxvwap31] ==========================================
== finished configs (all chains): 565
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
sort: write failed: 'standard output': Broken pipe
sort: write error
```
