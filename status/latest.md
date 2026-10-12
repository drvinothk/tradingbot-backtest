# btsync status  2026-10-12T04:27:21Z UTC / 2026-10-12 09:57:21 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 09:57:21 IST / 04:27:21 UTC  load: 4.79 4.94 4.83  free: 6G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap35_chain.heartbeat
2026-10-12 07:15:51 IST fxvwap35: reaper timer stopped
2026-10-12 07:15:52 IST fxvwap35: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap35s_chain.heartbeat
2026-10-12 07:15:02 IST fxvwap35s: reaper timer stopped
2026-10-12 07:15:04 IST fxvwap35s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 07:15:51 IST fxvwap35s: sweep finished rc=0
2026-10-12 07:15:51 IST fxvwap35s: chain finished
-- fxvwap34_chain.heartbeat
2026-10-12 04:41:27 IST fxvwap34: reaper timer stopped
2026-10-12 04:41:28 IST fxvwap34: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 07:15:02 IST fxvwap34: sweep finished rc=0
2026-10-12 07:15:02 IST fxvwap34: chain finished
== last 8 s6_status lines:
[2026-10-12T01:45:51Z] [fxvwap35s] VWAP_FX_s15_expatm_p250_tl3 OK (47s, 2 trades, 52G free)
[2026-10-12T01:45:51Z] [fxvwap35s] ==========================================
[2026-10-12T01:45:51Z] [fxvwap35s] sweep [fxvwap35s] COMPLETE -> data/historical/backtest_reports/s6_fxvwap35s (0min)
[2026-10-12T01:45:51Z] [fxvwap35s] ==========================================
[2026-10-12T01:45:52Z] [fxvwap35] ==========================================
[2026-10-12T01:45:52Z] [fxvwap35] sweep [fxvwap35] -> data/historical/backtest_reports/s6_fxvwap35 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-12T01:45:52Z] [fxvwap35] ==========================================
[2026-10-12T01:45:52Z] [fxvwap35] --- VWAP_FX_s15_expatm_p250_tl3 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_acti
== finished configs (all chains): 569
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9689s ago (>2.5h) while a unit is running -- possible stall
```
