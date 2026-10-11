# btsync status  2026-10-11T14:59:19Z UTC / 2026-10-11 20:29:19 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 20:29:19 IST / 14:59:19 UTC  load: 4.77 4.76 4.74  free: 7G avail  disk: 52G free
== units:
  backtest-20261011-124148.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c4_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap31_chain.heartbeat
2026-10-11 19:55:50 IST fxvwap31: reaper timer stopped
2026-10-11 19:55:51 IST fxvwap31: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
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
[2026-10-11T14:25:46Z] [fxvwap30] VWAP_FX_s15_atm OK (8792s, 1618 trades, 52G free)
[2026-10-11T14:25:46Z] [fxvwap30] ==========================================
[2026-10-11T14:25:46Z] [fxvwap30] sweep [fxvwap30] COMPLETE -> data/historical/backtest_reports/s6_fxvwap30 (146min)
[2026-10-11T14:25:46Z] [fxvwap30] ==========================================
[2026-10-11T14:25:51Z] [fxvwap31] ==========================================
[2026-10-11T14:25:51Z] [fxvwap31] sweep [fxvwap31] -> data/historical/backtest_reports/s6_fxvwap31 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T14:25:51Z] [fxvwap31] ==========================================
[2026-10-11T14:25:51Z] [fxvwap31] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activati
== finished configs (all chains): 564
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
