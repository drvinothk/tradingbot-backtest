# btsync status  2026-10-11T08:56:38Z UTC / 2026-10-11 14:26:38 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-11 14:26:38 IST / 08:56:38 UTC  load: 2.53 0.75 0.28  free: 7G avail  disk: 52G free
== units:
  backtest-20261011-085532.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./smoke_strike_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- sst2_chain.heartbeat
2026-10-11 14:26:22 IST sst2: reaper timer stopped
2026-10-11 14:26:23 IST sst2: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- sst1_chain.heartbeat
2026-10-11 14:25:33 IST sst1: reaper timer stopped
2026-10-11 14:25:34 IST sst1: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 14:26:22 IST sst1: sweep finished rc=0
2026-10-11 14:26:22 IST sst1: chain finished
-- fxvwap27_chain.heartbeat
2026-10-11 10:19:24 IST fxvwap27: reaper timer stopped
2026-10-11 10:19:26 IST fxvwap27: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine f5d4d5d0
2026-10-11 13:06:33 IST fxvwap27: sweep finished rc=0
2026-10-11 13:06:33 IST fxvwap27: chain finished
== last 8 s6_status lines:
[2026-10-11T08:56:22Z] [sst1] VWAP_FX_s15_base OK (48s, 2 trades, 52G free)
[2026-10-11T08:56:22Z] [sst1] ==========================================
[2026-10-11T08:56:22Z] [sst1] sweep [sst1] COMPLETE -> data/historical/backtest_reports/s6_sst1 (0min)
[2026-10-11T08:56:22Z] [sst1] ==========================================
[2026-10-11T08:56:23Z] [sst2] ==========================================
[2026-10-11T08:56:23Z] [sst2] sweep [sst2] -> data/historical/backtest_reports/s6_sst2 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/ubuntu
[2026-10-11T08:56:23Z] [sst2] ==========================================
[2026-10-11T08:56:23Z] [sst2] --- VWAP_FX_s15_expatm (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation_fracti
== finished configs (all chains): 562
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
