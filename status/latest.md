# btsync status  2026-10-11T11:30:23Z UTC / 2026-10-11 17:00:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 17:00:23 IST / 11:30:23 UTC  load: 4.18 4.57 4.73  free: 7G avail  disk: 52G free
== units:
  backtest-20261011-085827.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_strike_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap29_chain.heartbeat
2026-10-11 16:59:36 IST fxvwap29: reaper timer stopped
2026-10-11 16:59:38 IST fxvwap29: QC ok; 314 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap28_chain.heartbeat
2026-10-11 14:28:28 IST fxvwap28: reaper timer stopped
2026-10-11 14:28:29 IST fxvwap28: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 16:59:36 IST fxvwap28: sweep finished rc=0
2026-10-11 16:59:36 IST fxvwap28: chain finished
-- sst3_chain.heartbeat
2026-10-11 14:27:11 IST sst3: reaper timer stopped
2026-10-11 14:27:12 IST sst3: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 14:28:00 IST sst3: sweep finished rc=0
2026-10-11 14:28:00 IST sst3: chain finished
== last 8 s6_status lines:
[2026-10-11T11:29:36Z] [fxvwap28] VWAP_FX_s15_base OK (9067s, 1724 trades, 52G free)
[2026-10-11T11:29:36Z] [fxvwap28] ==========================================
[2026-10-11T11:29:36Z] [fxvwap28] sweep [fxvwap28] COMPLETE -> data/historical/backtest_reports/s6_fxvwap28 (151min)
[2026-10-11T11:29:36Z] [fxvwap28] ==========================================
[2026-10-11T11:29:38Z] [fxvwap29] ==========================================
[2026-10-11T11:29:38Z] [fxvwap29] sweep [fxvwap29] -> data/historical/backtest_reports/s6_fxvwap29 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T11:29:38Z] [fxvwap29] ==========================================
[2026-10-11T11:29:38Z] [fxvwap29] --- VWAP_FX_s15_expatm (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
== finished configs (all chains): 564
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
