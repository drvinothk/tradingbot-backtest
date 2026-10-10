# btsync status  2026-10-10T23:58:41Z UTC / 2026-10-11 05:28:41 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 05:28:41 IST / 23:58:41 UTC  load: 4.89 4.88 4.83  free: 8G avail  disk: 54G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap25_chain.heartbeat
2026-10-11 04:45:43 IST fxvwap25: reaper timer stopped
2026-10-11 04:45:44 IST fxvwap25: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
-- fxvwap24_chain.heartbeat
2026-10-11 02:15:52 IST fxvwap24: reaper timer stopped
2026-10-11 02:15:53 IST fxvwap24: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 04:45:43 IST fxvwap24: sweep finished rc=0
2026-10-11 04:45:43 IST fxvwap24: chain finished
-- fxvwap23_chain.heartbeat
2026-10-10 23:45:17 IST fxvwap23: reaper timer stopped
2026-10-10 23:45:19 IST fxvwap23: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 02:15:52 IST fxvwap23: sweep finished rc=0
2026-10-11 02:15:52 IST fxvwap23: chain finished
== last 8 s6_status lines:
[2026-10-10T23:15:43Z] [fxvwap24] VWAP_FX_f15_run OK (8989s, 978 trades, 54G free)
[2026-10-10T23:15:43Z] [fxvwap24] ==========================================
[2026-10-10T23:15:43Z] [fxvwap24] sweep [fxvwap24] COMPLETE -> data/historical/backtest_reports/s6_fxvwap24 (149min)
[2026-10-10T23:15:43Z] [fxvwap24] ==========================================
[2026-10-10T23:15:44Z] [fxvwap25] ==========================================
[2026-10-10T23:15:44Z] [fxvwap25] sweep [fxvwap25] -> data/historical/backtest_reports/s6_fxvwap25 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-10T23:15:44Z] [fxvwap25] ==========================================
[2026-10-10T23:15:44Z] [fxvwap25] --- VWAP_FX_f15_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fract
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
