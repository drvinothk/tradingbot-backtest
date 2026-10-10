# btsync status  2026-10-10T22:52:03Z UTC / 2026-10-11 04:22:03 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 04:22:03 IST / 22:52:03 UTC  load: 4.85 4.75 4.71  free: 8G avail  disk: 54G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap24_chain.heartbeat
2026-10-11 02:15:52 IST fxvwap24: reaper timer stopped
2026-10-11 02:15:53 IST fxvwap24: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
-- fxvwap23_chain.heartbeat
2026-10-10 23:45:17 IST fxvwap23: reaper timer stopped
2026-10-10 23:45:19 IST fxvwap23: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 02:15:52 IST fxvwap23: sweep finished rc=0
2026-10-11 02:15:52 IST fxvwap23: chain finished
-- fxvwap22_chain.heartbeat
2026-10-10 20:21:33 IST fxvwap22: reaper timer stopped
2026-10-10 20:21:35 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 21:18:27 IST fxvwap22: reaper timer stopped
2026-10-10 21:18:28 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-10 23:45:17 IST fxvwap22: sweep finished rc=0
2026-10-10 23:45:17 IST fxvwap22: chain finished
== last 8 s6_status lines:
[2026-10-10T20:45:51Z] [fxvwap23] VWAP_FX_f15_s40t80 OK (9032s, 1040 trades, 54G free)
[2026-10-10T20:45:51Z] [fxvwap23] ==========================================
[2026-10-10T20:45:51Z] [fxvwap23] sweep [fxvwap23] COMPLETE -> data/historical/backtest_reports/s6_fxvwap23 (150min)
[2026-10-10T20:45:52Z] [fxvwap23] ==========================================
[2026-10-10T20:45:54Z] [fxvwap24] ==========================================
[2026-10-10T20:45:54Z] [fxvwap24] sweep [fxvwap24] -> data/historical/backtest_reports/s6_fxvwap24 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T20:45:54Z] [fxvwap24] ==========================================
[2026-10-10T20:45:54Z] [fxvwap24] --- VWAP_FX_f15_run (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
