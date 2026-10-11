# btsync status  2026-10-11T18:08:33Z UTC / 2026-10-11 23:38:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 23:38:33 IST / 18:08:33 UTC  load: 1.55 0.37 0.12  free: 9G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap32s_chain.heartbeat
2026-10-11 23:38:03 IST fxvwap32s: reaper timer stopped
2026-10-11 23:38:05 IST fxvwap32s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap31_chain.heartbeat
2026-10-11 19:55:50 IST fxvwap31: reaper timer stopped
2026-10-11 19:55:51 IST fxvwap31: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 22:23:48 IST fxvwap31: sweep finished rc=0
2026-10-11 22:23:48 IST fxvwap31: chain finished
-- fxvwap30_chain.heartbeat
2026-10-11 17:29:12 IST fxvwap30: reaper timer stopped
2026-10-11 17:29:13 IST fxvwap30: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 19:55:46 IST fxvwap30: sweep finished rc=0
2026-10-11 19:55:46 IST fxvwap30: chain finished
== last 8 s6_status lines:
[2026-10-11T16:53:48Z] [fxvwap31] VWAP_FX_s15_expatm_p250 OK (8877s, 1819 trades, 52G free)
[2026-10-11T16:53:48Z] [fxvwap31] ==========================================
[2026-10-11T16:53:48Z] [fxvwap31] sweep [fxvwap31] COMPLETE -> data/historical/backtest_reports/s6_fxvwap31 (147min)
[2026-10-11T16:53:48Z] [fxvwap31] ==========================================
[2026-10-11T18:08:05Z] [fxvwap32s] ==========================================
[2026-10-11T18:08:05Z] [fxvwap32s] sweep [fxvwap32s] -> data/historical/backtest_reports/s6_fxvwap32s (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-11T18:08:05Z] [fxvwap32s] ==========================================
[2026-10-11T18:08:05Z] [fxvwap32s] --- VWAP_FX_s15_atm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
== finished configs (all chains): 565
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
