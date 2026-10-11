# btsync status  2026-10-11T04:52:53Z UTC / 2026-10-11 10:22:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 10:22:53 IST / 04:52:53 UTC  load: 4.61 4.69 4.82  free: 7G avail  disk: 52G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap27_chain.heartbeat
2026-10-11 10:19:24 IST fxvwap27: reaper timer stopped
2026-10-11 10:19:26 IST fxvwap27: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
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
[2026-10-11T04:49:24Z] [fxvwap26] VWAP_FX_f15_tol OK (10926s, 879 trades, 52G free)
[2026-10-11T04:49:24Z] [fxvwap26] ==========================================
[2026-10-11T04:49:24Z] [fxvwap26] sweep [fxvwap26] COMPLETE -> data/historical/backtest_reports/s6_fxvwap26 (182min)
[2026-10-11T04:49:24Z] [fxvwap26] ==========================================
[2026-10-11T04:49:26Z] [fxvwap27] ==========================================
[2026-10-11T04:49:26Z] [fxvwap27] sweep [fxvwap27] -> data/historical/backtest_reports/s6_fxvwap27 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T04:49:26Z] [fxvwap27] ==========================================
[2026-10-11T04:49:26Z] [fxvwap27] --- VWAP_FX_f5_nogate (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.0015, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
