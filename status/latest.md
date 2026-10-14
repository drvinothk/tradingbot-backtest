# btsync status  2026-10-14T09:04:56Z UTC / 2026-10-14 14:34:56 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-14 14:34:56 IST / 09:04:56 UTC  load: 0.24 0.36 0.35  free: 8G avail  disk: 51G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- vc_old_chain.heartbeat
2026-10-14 14:34:34 IST vc_old: ABORT -- a sweep is running
-- vc_new_chain.heartbeat
2026-10-14 14:34:34 IST vc_new: ABORT -- a sweep is running
-- rem_col1p_chain.heartbeat
2026-10-13 12:23:39 IST rem_col1p: reaper timer stopped
2026-10-13 12:23:41 IST rem_col1p: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 14:15:36 IST rem_col1p: sweep finished rc=0
2026-10-13 14:15:36 IST rem_col1p: chain finished
2026-10-13 14:15:36 IST rem_col1p: reaper timer restarted
== last 8 s6_status lines:
[2026-10-13T06:53:41Z] [rem_col1p] ==========================================
[2026-10-13T06:53:41Z] [rem_col1p] sweep [rem_col1p] -> data/historical/backtest_reports/s6_rem_col1p (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-13T06:53:41Z] [rem_col1p] ==========================================
[2026-10-13T06:53:41Z] [rem_col1p] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activat
[2026-10-13T08:45:36Z] [rem_col1p] VWAP_FX_s15_expatm_p250 OK (6715s, 640 trades, 51G free)
[2026-10-13T08:45:36Z] [rem_col1p] ==========================================
[2026-10-13T08:45:36Z] [rem_col1p] sweep [rem_col1p] COMPLETE -> data/historical/backtest_reports/s6_rem_col1p (111min)
[2026-10-13T08:45:36Z] [rem_col1p] ==========================================
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
81d4fcc0 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain vc_old_chain.heartbeat ended without a finish line (last: 2026-10-14 14:34:34 IST vc_old: ABORT -- a sweep is running)
! vc_old_chain.heartbeat: 2026-10-14 14:34:34 IST vc_old: ABORT -- a sweep is running
! chain vc_new_chain.heartbeat ended without a finish line (last: 2026-10-14 14:34:34 IST vc_new: ABORT -- a sweep is running)
! vc_new_chain.heartbeat: 2026-10-14 14:34:34 IST vc_new: ABORT -- a sweep is running
```
