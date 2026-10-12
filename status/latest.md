# btsync status  2026-10-12T01:45:13Z UTC / 2026-10-12 07:15:13 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 07:15:13 IST / 01:45:13 UTC  load: 3.71 4.45 4.67  free: 9G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxvwap35s_chain.heartbeat
2026-10-12 07:15:02 IST fxvwap35s: reaper timer stopped
2026-10-12 07:15:04 IST fxvwap35s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap34_chain.heartbeat
2026-10-12 04:41:27 IST fxvwap34: reaper timer stopped
2026-10-12 04:41:28 IST fxvwap34: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 07:15:02 IST fxvwap34: sweep finished rc=0
2026-10-12 07:15:02 IST fxvwap34: chain finished
-- fxvwap34s_chain.heartbeat
2026-10-12 04:40:39 IST fxvwap34s: reaper timer stopped
2026-10-12 04:40:40 IST fxvwap34s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 04:41:27 IST fxvwap34s: sweep finished rc=0
2026-10-12 04:41:27 IST fxvwap34s: chain finished
== last 8 s6_status lines:
[2026-10-12T01:45:02Z] [fxvwap34] VWAP_FX_s15_expatm_p250_s40t80 OK (9214s, 1720 trades, 52G free)
[2026-10-12T01:45:02Z] [fxvwap34] ==========================================
[2026-10-12T01:45:02Z] [fxvwap34] sweep [fxvwap34] COMPLETE -> data/historical/backtest_reports/s6_fxvwap34 (153min)
[2026-10-12T01:45:02Z] [fxvwap34] ==========================================
[2026-10-12T01:45:04Z] [fxvwap35s] ==========================================
[2026-10-12T01:45:04Z] [fxvwap35s] sweep [fxvwap35s] -> data/historical/backtest_reports/s6_fxvwap35s (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-12T01:45:04Z] [fxvwap35s] ==========================================
[2026-10-12T01:45:04Z] [fxvwap35s] --- VWAP_FX_s15_expatm_p250_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_act
== finished configs (all chains): 568
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
