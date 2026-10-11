# btsync status  2026-10-11T02:03:26Z UTC / 2026-10-11 07:33:26 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 07:33:26 IST / 02:03:26 UTC  load: 6.29 5.74 5.16  free: 6G avail  disk: 54G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap26_chain.heartbeat
2026-10-11 07:17:16 IST fxvwap26: reaper timer stopped
2026-10-11 07:17:17 IST fxvwap26: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
-- fxvwap25_chain.heartbeat
2026-10-11 04:45:43 IST fxvwap25: reaper timer stopped
2026-10-11 04:45:44 IST fxvwap25: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 07:17:16 IST fxvwap25: sweep finished rc=0
2026-10-11 07:17:16 IST fxvwap25: chain finished
-- fxvwap24_chain.heartbeat
2026-10-11 02:15:52 IST fxvwap24: reaper timer stopped
2026-10-11 02:15:53 IST fxvwap24: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 04:45:43 IST fxvwap24: sweep finished rc=0
2026-10-11 04:45:43 IST fxvwap24: chain finished
== last 8 s6_status lines:
[2026-10-11T01:47:16Z] [fxvwap25] VWAP_FX_f15_tl3 OK (9092s, 1133 trades, 54G free)
[2026-10-11T01:47:16Z] [fxvwap25] ==========================================
[2026-10-11T01:47:16Z] [fxvwap25] sweep [fxvwap25] COMPLETE -> data/historical/backtest_reports/s6_fxvwap25 (151min)
[2026-10-11T01:47:16Z] [fxvwap25] ==========================================
[2026-10-11T01:47:17Z] [fxvwap26] ==========================================
[2026-10-11T01:47:17Z] [fxvwap26] sweep [fxvwap26] -> data/historical/backtest_reports/s6_fxvwap26 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T01:47:17Z] [fxvwap26] ==========================================
[2026-10-11T01:47:17Z] [fxvwap26] --- VWAP_FX_f15_tol (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
