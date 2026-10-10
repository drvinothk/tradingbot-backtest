# btsync status  2026-10-10T18:28:20Z UTC / 2026-10-10 23:58:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 23:58:20 IST / 18:28:20 UTC  load: 4.43 4.67 4.70  free: 8G avail  disk: 54G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap23_chain.heartbeat
2026-10-10 23:45:17 IST fxvwap23: reaper timer stopped
2026-10-10 23:45:19 IST fxvwap23: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
-- fxvwap22_chain.heartbeat
2026-10-10 20:21:33 IST fxvwap22: reaper timer stopped
2026-10-10 20:21:35 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 21:18:27 IST fxvwap22: reaper timer stopped
2026-10-10 21:18:28 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-10 23:45:17 IST fxvwap22: sweep finished rc=0
2026-10-10 23:45:17 IST fxvwap22: chain finished
-- fxvwap21r_chain.heartbeat
2026-10-10 21:04:27 IST fxvwap21r: reaper timer stopped
2026-10-10 21:04:29 IST fxvwap21r: QC ok; 136 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-10 21:18:26 IST fxvwap21r: sweep finished rc=0
2026-10-10 21:18:26 IST fxvwap21r: chain finished
== last 8 s6_status lines:
[2026-10-10T18:15:17Z] [fxvwap22] VWAP_FX_f15_base OK (8809s, 1099 trades, 54G free)
[2026-10-10T18:15:17Z] [fxvwap22] ==========================================
[2026-10-10T18:15:17Z] [fxvwap22] sweep [fxvwap22] COMPLETE -> data/historical/backtest_reports/s6_fxvwap22 (146min)
[2026-10-10T18:15:17Z] [fxvwap22] ==========================================
[2026-10-10T18:15:19Z] [fxvwap23] ==========================================
[2026-10-10T18:15:19Z] [fxvwap23] sweep [fxvwap23] -> data/historical/backtest_reports/s6_fxvwap23 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T18:15:19Z] [fxvwap23] ==========================================
[2026-10-10T18:15:19Z] [fxvwap23] --- VWAP_FX_f15_s40t80 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
