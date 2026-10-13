# btsync status  2026-10-13T09:09:13Z UTC / 2026-10-13 14:39:13 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 14:39:13 IST / 09:09:13 UTC  load: 0.34 0.37 1.15  free: 8G avail  disk: 51G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- rem_col1p_chain.heartbeat
2026-10-13 12:23:39 IST rem_col1p: reaper timer stopped
2026-10-13 12:23:41 IST rem_col1p: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 14:15:36 IST rem_col1p: sweep finished rc=0
2026-10-13 14:15:36 IST rem_col1p: chain finished
2026-10-13 14:15:36 IST rem_col1p: reaper timer restarted
-- col_tri_chain.heartbeat
2026-10-13 03:39:26 IST col_tri: reaper timer stopped
2026-10-13 03:39:27 IST col_tri: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 04:46:02 IST col_tri: sweep finished rc=0
2026-10-13 04:46:02 IST col_tri: chain finished
-- col_all3_chain.heartbeat
2026-10-13 02:31:32 IST col_all3: reaper timer stopped
2026-10-13 02:31:34 IST col_all3: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 03:39:26 IST col_all3: sweep finished rc=0
2026-10-13 03:39:26 IST col_all3: chain finished
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
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
