# btsync status  2026-10-04T07:42:53Z UTC / 2026-10-04 13:12:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-04 13:12:53 IST / 07:42:53 UTC  load: 0.76 2.67 2.61  free: 9G avail  disk: 60G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxv1_chain.heartbeat
2026-10-04 13:09:58 IST fxv1: reaper timer stopped
2026-10-04 13:09:59 IST fxv1: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:11:05 IST fxv1: sweep finished rc=0
2026-10-04 13:11:05 IST fxv1: chain finished
-- fxv0_chain.heartbeat
2026-10-04 13:08:50 IST fxv0: reaper timer stopped
2026-10-04 13:08:51 IST fxv0: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:09:57 IST fxv0: sweep finished rc=0
2026-10-04 13:09:57 IST fxv0: chain finished
-- fx3_chain.heartbeat
2026-10-04 13:07:09 IST fx3: reaper timer stopped
2026-10-04 13:07:10 IST fx3: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:08:50 IST fx3: sweep finished rc=0
2026-10-04 13:08:50 IST fx3: chain finished
== last 8 s6_status lines:
[2026-10-04T07:39:59Z] [fxv1] ==========================================
[2026-10-04T07:39:59Z] [fxv1] sweep [fxv1] -> data/historical/backtest_reports/s6_fxv1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/ubuntu
[2026-10-04T07:39:59Z] [fxv1] ==========================================
[2026-10-04T07:39:59Z] [fxv1] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, "trail_act
[2026-10-04T07:41:05Z] [fxv1] VWAP_Base OK (66s, 107 trades, 60G free)
[2026-10-04T07:41:05Z] [fxv1] ==========================================
[2026-10-04T07:41:05Z] [fxv1] sweep [fxv1] COMPLETE -> data/historical/backtest_reports/s6_fxv1 (1min)
[2026-10-04T07:41:05Z] [fxv1] ==========================================
== finished configs (all chains): 527
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
