# btsync status  2026-10-09T09:53:23Z UTC / 2026-10-09 15:23:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 15:23:23 IST / 09:53:23 UTC  load: 0.24 0.18 0.22  free: 8G avail  disk: 54G free
== units:
  backtest-20261009-062701.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf_1009.sh"
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- smokehtf15c_chain.heartbeat
2026-10-09 11:55:53 IST smokehtf15c: reaper timer stopped
2026-10-09 11:55:55 IST smokehtf15c: QC ok; 2 day:expiry pairs, 1 config(s), SHARD_COUNT=1, engine 937113b0
2026-10-09 11:56:26 IST smokehtf15c: sweep finished rc=0
2026-10-09 11:56:26 IST smokehtf15c: chain finished
2026-10-09 11:56:26 IST smokehtf15c: reaper timer restarted
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
[2026-10-09T06:25:55Z] [smokehtf15c] ==========================================
[2026-10-09T06:25:55Z] [smokehtf15c] sweep [smokehtf15c] -> data/historical/backtest_reports/s6_smokehtf15c (1 configs, 1 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --
[2026-10-09T06:25:55Z] [smokehtf15c] ==========================================
[2026-10-09T06:25:55Z] [smokehtf15c] --- VWAP_FX_htf15 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "trend_lookback_bars": 4, "max_vwap_crosses_in_lookback":
[2026-10-09T06:26:26Z] [smokehtf15c] VWAP_FX_htf15 OK (31s, 5 trades, 55G free)
[2026-10-09T06:26:26Z] [smokehtf15c] ==========================================
[2026-10-09T06:26:26Z] [smokehtf15c] sweep [smokehtf15c] COMPLETE -> data/historical/backtest_reports/s6_smokehtf15c (0min)
[2026-10-09T06:26:26Z] [smokehtf15c] ==========================================
== finished configs (all chains): 548
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-09T06:23:08Z] [smokehtf5b] VWAP_FX_htf5 HAD SHARD FAILURES (18s, 0 trades, 55G free)
[2026-10-09T06:23:25Z] [smokehtf15b] *** VWAP_FX_htf15 merge FAILED
[2026-10-09T06:23:26Z] [smokehtf15b] VWAP_FX_htf15 HAD SHARD FAILURES (17s, 0 trades, 55G free)
! newest config started/finished 12418s ago (>2.5h) while a unit is running -- possible stall
```
