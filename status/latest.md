# btsync status  2026-10-09T06:23:45Z UTC / 2026-10-09 11:53:45 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 11:53:45 IST / 06:23:45 UTC  load: 0.63 0.63 0.59  free: 8G avail  disk: 55G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- smokehtf15b_chain.heartbeat
2026-10-09 11:53:08 IST smokehtf15b: reaper timer stopped
2026-10-09 11:53:09 IST smokehtf15b: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 5a676747
2026-10-09 11:53:26 IST smokehtf15b: sweep finished rc=0
2026-10-09 11:53:26 IST smokehtf15b: chain finished
2026-10-09 11:53:26 IST smokehtf15b: reaper timer restarted
-- smokehtf5b_chain.heartbeat
2026-10-09 11:52:49 IST smokehtf5b: reaper timer stopped
2026-10-09 11:52:50 IST smokehtf5b: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 5a676747
2026-10-09 11:53:08 IST smokehtf5b: sweep finished rc=0
2026-10-09 11:53:08 IST smokehtf5b: chain finished
2026-10-09 11:53:08 IST smokehtf5b: reaper timer restarted
-- smokehtf5_chain.heartbeat
2026-10-09 11:49:01 IST smokehtf5: reaper timer stopped
2026-10-09 11:49:03 IST smokehtf5: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 292f2ae5
2026-10-09 11:49:37 IST smokehtf5: sweep finished rc=0
2026-10-09 11:49:37 IST smokehtf5: chain finished
2026-10-09 11:49:37 IST smokehtf5: reaper timer restarted
== last 8 s6_status lines:
[2026-10-09T06:23:09Z] [smokehtf15b] sweep [smokehtf15b] -> data/historical/backtest_reports/s6_smokehtf15b (1 configs, 1 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --
[2026-10-09T06:23:09Z] [smokehtf15b] ==========================================
[2026-10-09T06:23:09Z] [smokehtf15b] --- VWAP_FX_htf15 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "trend_lookback_bars": 4, "max_vwap_crosses_in_lookback":
[2026-10-09T06:23:25Z] [smokehtf15b] *** VWAP_FX_htf15 merge FAILED
[2026-10-09T06:23:26Z] [smokehtf15b] VWAP_FX_htf15 HAD SHARD FAILURES (17s, 0 trades, 55G free)
[2026-10-09T06:23:26Z] [smokehtf15b] ==========================================
[2026-10-09T06:23:26Z] [smokehtf15b] sweep [smokehtf15b] COMPLETE -> data/historical/backtest_reports/s6_smokehtf15b (0min)
[2026-10-09T06:23:26Z] [smokehtf15b] ==========================================
== finished configs (all chains): 547
== md5:
5a676747 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
