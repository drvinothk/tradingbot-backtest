# btsync status  2026-10-11T10:40:19Z UTC / 2026-10-11 16:10:19 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 16:10:19 IST / 10:40:19 UTC  load: 5.45 5.19 5.02  free: 6G avail  disk: 52G free
== units:
  backtest-20261011-085827.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_strike_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap28_chain.heartbeat
2026-10-11 14:28:28 IST fxvwap28: reaper timer stopped
2026-10-11 14:28:29 IST fxvwap28: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- sst3_chain.heartbeat
2026-10-11 14:27:11 IST sst3: reaper timer stopped
2026-10-11 14:27:12 IST sst3: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 14:28:00 IST sst3: sweep finished rc=0
2026-10-11 14:28:00 IST sst3: chain finished
-- sst2_chain.heartbeat
2026-10-11 14:26:22 IST sst2: reaper timer stopped
2026-10-11 14:26:23 IST sst2: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 14:27:11 IST sst2: sweep finished rc=0
2026-10-11 14:27:11 IST sst2: chain finished
== last 8 s6_status lines:
[2026-10-11T08:58:00Z] [sst3] VWAP_FX_s15_atm OK (48s, 1 trades, 52G free)
[2026-10-11T08:58:00Z] [sst3] ==========================================
[2026-10-11T08:58:00Z] [sst3] sweep [sst3] COMPLETE -> data/historical/backtest_reports/s6_sst3 (0min)
[2026-10-11T08:58:00Z] [sst3] ==========================================
[2026-10-11T08:58:29Z] [fxvwap28] ==========================================
[2026-10-11T08:58:29Z] [fxvwap28] sweep [fxvwap28] -> data/historical/backtest_reports/s6_fxvwap28 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T08:58:29Z] [fxvwap28] ==========================================
[2026-10-11T08:58:29Z] [fxvwap28] --- VWAP_FX_s15_base (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_frac
== finished configs (all chains): 564
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
