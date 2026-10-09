# btsync status  2026-10-09T06:25:56Z UTC / 2026-10-09 11:55:56 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 11:55:56 IST / 06:25:56 UTC  load: 1.39 0.83 0.67  free: 8G avail  disk: 55G free
== units:
  backtest-20261009-062518.service loaded active running /tmp/smoke_htf.sh
== run_backtest procs: 1   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- smokehtf15c_chain.heartbeat
2026-10-09 11:55:53 IST smokehtf15c: reaper timer stopped
2026-10-09 11:55:55 IST smokehtf15c: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
-- smokehtf5c_chain.heartbeat
2026-10-09 11:55:18 IST smokehtf5c: reaper timer stopped
2026-10-09 11:55:20 IST smokehtf5c: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
2026-10-09 11:55:53 IST smokehtf5c: sweep finished rc=0
2026-10-09 11:55:53 IST smokehtf5c: chain finished
2026-10-09 11:55:53 IST smokehtf5c: reaper timer restarted
-- smokehtf15b_chain.heartbeat
2026-10-09 11:53:26 IST smokehtf15b: reaper timer restarted
2026-10-09 11:54:36 IST smokehtf15b: reaper timer stopped
2026-10-09 11:54:38 IST smokehtf15b: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
2026-10-09 11:55:09 IST smokehtf15b: sweep finished rc=0
2026-10-09 11:55:09 IST smokehtf15b: chain finished
2026-10-09 11:55:09 IST smokehtf15b: reaper timer restarted
== last 8 s6_status lines:
[2026-10-09T06:25:53Z] [smokehtf5c] VWAP_FX_htf5 OK (33s, 10 trades, 55G free)
[2026-10-09T06:25:53Z] [smokehtf5c] ==========================================
[2026-10-09T06:25:53Z] [smokehtf5c] sweep [smokehtf5c] COMPLETE -> data/historical/backtest_reports/s6_smokehtf5c (0min)
[2026-10-09T06:25:53Z] [smokehtf5c] ==========================================
[2026-10-09T06:25:55Z] [smokehtf15c] ==========================================
[2026-10-09T06:25:55Z] [smokehtf15c] sweep [smokehtf15c] -> data/historical/backtest_reports/s6_smokehtf15c (1 configs, 1 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --
[2026-10-09T06:25:55Z] [smokehtf15c] ==========================================
[2026-10-09T06:25:55Z] [smokehtf15c] --- VWAP_FX_htf15 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "trend_lookback_bars": 4, "max_vwap_crosses_in_lookback":
== finished configs (all chains): 548
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: fflush failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
