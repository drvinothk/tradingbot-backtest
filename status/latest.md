# btsync status  2026-10-10T08:28:02Z UTC / 2026-10-10 13:58:02 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 13:58:02 IST / 08:28:02 UTC  load: 5.03 4.99 4.87  free: 8G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap20_chain.heartbeat
2026-10-10 11:26:33 IST fxvwap20: reaper timer stopped
2026-10-10 11:26:35 IST fxvwap20: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
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
[2026-10-10T05:56:33Z] [fxvwap19] VWAP_FX_h15_tl6 OK (9106s, 217 trades, 54G free)
[2026-10-10T05:56:33Z] [fxvwap19] ==========================================
[2026-10-10T05:56:33Z] [fxvwap19] sweep [fxvwap19] COMPLETE -> data/historical/backtest_reports/s6_fxvwap19 (151min)
[2026-10-10T05:56:33Z] [fxvwap19] ==========================================
[2026-10-10T05:56:35Z] [fxvwap20] ==========================================
[2026-10-10T05:56:35Z] [fxvwap20] sweep [fxvwap20] -> data/historical/backtest_reports/s6_fxvwap20 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T05:56:35Z] [fxvwap20] ==========================================
[2026-10-10T05:56:35Z] [fxvwap20] --- VWAP_FX_h15_norr (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9087s ago (>2.5h) while a unit is running -- possible stall
```
