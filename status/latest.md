# btsync status  2026-10-10T15:36:32Z UTC / 2026-10-10 21:06:32 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 21:06:32 IST / 15:36:32 UTC  load: 4.40 4.35 4.48  free: 7G avail  disk: 54G free
== units:
  backtest-20261010-153335.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_f15b_1010.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 8
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- fxvwap21r_chain.heartbeat
2026-10-10 21:04:27 IST fxvwap21r: reaper timer stopped
2026-10-10 21:04:29 IST fxvwap21r: QC ok; 136 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
-- smoke0606b_chain.heartbeat
2026-10-10 21:03:35 IST smoke0606b: reaper timer stopped
2026-10-10 21:03:36 IST smoke0606b: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-10 21:04:27 IST smoke0606b: sweep finished rc=0
2026-10-10 21:04:27 IST smoke0606b: chain finished
-- fxvwap22_chain.heartbeat
2026-10-10 20:21:33 IST fxvwap22: reaper timer stopped
2026-10-10 20:21:35 IST fxvwap22: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
== last 8 s6_status lines:
[2026-10-10T15:34:27Z] [smoke0606b] VWAP_FX_f15_log OK (51s, 6 trades, 54G free)
[2026-10-10T15:34:27Z] [smoke0606b] ==========================================
[2026-10-10T15:34:27Z] [smoke0606b] sweep [smoke0606b] COMPLETE -> data/historical/backtest_reports/s6_smoke0606b (0min)
[2026-10-10T15:34:27Z] [smoke0606b] ==========================================
[2026-10-10T15:34:29Z] [fxvwap21r] ==========================================
[2026-10-10T15:34:29Z] [fxvwap21r] sweep [fxvwap21r] -> data/historical/backtest_reports/s6_fxvwap21r (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-10T15:34:29Z] [fxvwap21r] ==========================================
[2026-10-10T15:34:29Z] [fxvwap21r] --- VWAP_FX_f15_log (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
== finished configs (all chains): 561
== md5:
f5d4d5d0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
sort: write failed: 'standard output': Broken pipe
sort: write error
```
