# btsync status  2026-10-09T16:59:43Z UTC / 2026-10-09 22:29:43 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 22:29:43 IST / 16:59:43 UTC  load: 4.60 2.22 0.88  free: 8G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qch15_s30t50_chain.heartbeat
2026-10-09 22:28:10 IST qch15_s30t50: reaper timer stopped
2026-10-09 22:28:12 IST qch15_s30t50: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- qch15_c1245_chain.heartbeat
2026-10-09 22:26:23 IST qch15_c1245: reaper timer stopped
2026-10-09 22:26:25 IST qch15_c1245: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:28:10 IST qch15_c1245: sweep finished rc=0
2026-10-09 22:28:10 IST qch15_c1245: chain finished
-- fxvwap14_chain.heartbeat
2026-10-09 18:20:35 IST fxvwap14: reaper timer stopped
2026-10-09 18:20:37 IST fxvwap14: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 20:52:22 IST fxvwap14: sweep finished rc=0
2026-10-09 20:52:22 IST fxvwap14: chain finished
== last 8 s6_status lines:
[2026-10-09T16:58:10Z] [qch15_c1245] VWAP_FX_h15_c1245 OK (105s, 5 trades, 54G free)
[2026-10-09T16:58:10Z] [qch15_c1245] ==========================================
[2026-10-09T16:58:10Z] [qch15_c1245] sweep [qch15_c1245] COMPLETE -> data/historical/backtest_reports/s6_qch15_c1245 (1min)
[2026-10-09T16:58:10Z] [qch15_c1245] ==========================================
[2026-10-09T16:58:12Z] [qch15_s30t50] ==========================================
[2026-10-09T16:58:12Z] [qch15_s30t50] sweep [qch15_s30t50] -> data/historical/backtest_reports/s6_qch15_s30t50 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12
[2026-10-09T16:58:12Z] [qch15_s30t50] ==========================================
[2026-10-09T16:58:12Z] [qch15_s30t50] --- VWAP_FX_h15_s30t50 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activatio
== finished configs (all chains): 549
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
```
