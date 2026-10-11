# btsync status  2026-10-11T08:36:40Z UTC / 2026-10-11 14:06:40 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 14:06:40 IST / 08:36:40 UTC  load: 0.00 0.02 0.09  free: 9G avail  disk: 52G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxvwap27_chain.heartbeat
2026-10-11 10:19:24 IST fxvwap27: reaper timer stopped
2026-10-11 10:19:26 IST fxvwap27: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 13:06:33 IST fxvwap27: sweep finished rc=0
2026-10-11 13:06:33 IST fxvwap27: chain finished
-- fxvwap26_chain.heartbeat
2026-10-11 07:17:16 IST fxvwap26: reaper timer stopped
2026-10-11 07:17:17 IST fxvwap26: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 10:19:24 IST fxvwap26: sweep finished rc=0
2026-10-11 10:19:24 IST fxvwap26: chain finished
-- fxvwap25_chain.heartbeat
2026-10-11 04:45:43 IST fxvwap25: reaper timer stopped
2026-10-11 04:45:44 IST fxvwap25: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 07:17:16 IST fxvwap25: sweep finished rc=0
2026-10-11 07:17:16 IST fxvwap25: chain finished
== last 8 s6_status lines:
[2026-10-11T04:49:26Z] [fxvwap27] ==========================================
[2026-10-11T04:49:26Z] [fxvwap27] sweep [fxvwap27] -> data/historical/backtest_reports/s6_fxvwap27 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T04:49:26Z] [fxvwap27] ==========================================
[2026-10-11T04:49:26Z] [fxvwap27] --- VWAP_FX_f5_nogate (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.0015, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
[2026-10-11T07:36:33Z] [fxvwap27] VWAP_FX_f5_nogate OK (10027s, 1966 trades, 52G free)
[2026-10-11T07:36:33Z] [fxvwap27] ==========================================
[2026-10-11T07:36:33Z] [fxvwap27] sweep [fxvwap27] COMPLETE -> data/historical/backtest_reports/s6_fxvwap27 (167min)
[2026-10-11T07:36:33Z] [fxvwap27] ==========================================
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
```
