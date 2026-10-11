# btsync status  2026-10-11T20:03:23Z UTC / 2026-10-12 01:33:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 01:33:23 IST / 20:03:23 UTC  load: 4.51 4.73 4.78  free: 8G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap32_chain.heartbeat
2026-10-11 23:38:52 IST fxvwap32: reaper timer stopped
2026-10-11 23:38:53 IST fxvwap32: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap32s_chain.heartbeat
2026-10-11 23:38:03 IST fxvwap32s: reaper timer stopped
2026-10-11 23:38:05 IST fxvwap32s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 23:38:52 IST fxvwap32s: sweep finished rc=0
2026-10-11 23:38:52 IST fxvwap32s: chain finished
-- fxvwap31_chain.heartbeat
2026-10-11 19:55:50 IST fxvwap31: reaper timer stopped
2026-10-11 19:55:51 IST fxvwap31: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 22:23:48 IST fxvwap31: sweep finished rc=0
2026-10-11 22:23:48 IST fxvwap31: chain finished
== last 8 s6_status lines:
[2026-10-11T18:08:52Z] [fxvwap32s] VWAP_FX_s15_atm_p250 OK (47s, 2 trades, 52G free)
[2026-10-11T18:08:52Z] [fxvwap32s] ==========================================
[2026-10-11T18:08:52Z] [fxvwap32s] sweep [fxvwap32s] COMPLETE -> data/historical/backtest_reports/s6_fxvwap32s (0min)
[2026-10-11T18:08:52Z] [fxvwap32s] ==========================================
[2026-10-11T18:08:53Z] [fxvwap32] ==========================================
[2026-10-11T18:08:53Z] [fxvwap32] sweep [fxvwap32] -> data/historical/backtest_reports/s6_fxvwap32 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T18:08:53Z] [fxvwap32] ==========================================
[2026-10-11T18:08:53Z] [fxvwap32] --- VWAP_FX_s15_atm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_
== finished configs (all chains): 566
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
