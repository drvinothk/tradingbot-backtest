# btsync status  2026-10-10T11:15:41Z UTC / 2026-10-10 16:45:41 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 16:45:41 IST / 11:15:41 UTC  load: 0.00 0.00 0.00  free: 10G avail  disk: 54G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
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
-- fxvwap18_chain.heartbeat
2026-10-10 06:19:17 IST fxvwap18: reaper timer stopped
2026-10-10 06:19:19 IST fxvwap18: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 08:54:44 IST fxvwap18: sweep finished rc=0
2026-10-10 08:54:44 IST fxvwap18: chain finished
== last 8 s6_status lines:
[2026-10-10T05:56:35Z] [fxvwap20] ==========================================
[2026-10-10T05:56:35Z] [fxvwap20] sweep [fxvwap20] -> data/historical/backtest_reports/s6_fxvwap20 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T05:56:35Z] [fxvwap20] ==========================================
[2026-10-10T05:56:35Z] [fxvwap20] --- VWAP_FX_h15_norr (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
[2026-10-10T08:28:57Z] [fxvwap20] VWAP_FX_h15_norr OK (9142s, 897 trades, 54G free)
[2026-10-10T08:28:57Z] [fxvwap20] ==========================================
[2026-10-10T08:28:57Z] [fxvwap20] sweep [fxvwap20] COMPLETE -> data/historical/backtest_reports/s6_fxvwap20 (152min)
[2026-10-10T08:28:57Z] [fxvwap20] ==========================================
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
