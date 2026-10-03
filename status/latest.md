# btsync status  2026-10-03T10:01:41Z UTC / 2026-10-03 15:31:41 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 15:31:41 IST / 10:01:41 UTC  load: 0.02 0.01 0.00  free: 9G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r33_VWAP_chain.heartbeat
2026-10-03 01:29:57 IST r33_VWAP: reaper timer stopped
2026-10-03 01:29:58 IST r33_VWAP: QC ok; 1472 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-03 13:46:42 IST r33_VWAP: sweep finished rc=0
2026-10-03 13:46:42 IST r33_VWAP: chain finished
2026-10-03 13:46:42 IST r33_VWAP: reaper timer restarted
-- r32_VWAP_chain.heartbeat
2026-10-03 01:14:24 IST r32_VWAP: reaper timer stopped
2026-10-03 01:14:26 IST r32_VWAP: QC ok; 70 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-03 01:29:43 IST r32_VWAP: sweep finished rc=0
2026-10-03 01:29:43 IST r32_VWAP: chain finished
2026-10-03 01:29:43 IST r32_VWAP: reaper timer restarted
-- r31_chain.heartbeat
2026-10-03 00:36:32 IST r31: reaper timer stopped
2026-10-03 00:36:34 IST r31: QC ok; 70 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-03 01:05:32 IST r31: sweep finished rc=0
2026-10-03 01:05:32 IST r31: chain finished
2026-10-03 01:05:32 IST r31: reaper timer restarted
2026-10-03 01:10 IST r31_VWAP: complete; outputs in backtest_reports/s6_r31_VWAP (heartbeat/log files above carry the tag r31)
== last 8 s6_status lines:
[2026-10-03T01:59:13Z] [r33_VWAP] VWAP_PCR_Live_Convic OK (10600s, 13890 trades, 61G free)
[2026-10-03T01:59:13Z] [r33_VWAP] --- VWAP_Conviction (vwap_pullback_conviction, src=futures_proxy) params={"exit_legs": [{"kind": "core", "stop_pct": 0.08, "qty_fraction": 0.4, "use_structure": true,
[2026-10-03T04:52:43Z] [r33_VWAP] VWAP_Conviction OK (10410s, 9733 trades, 61G free)
[2026-10-03T04:52:43Z] [r33_VWAP] --- VWAP_Base_Test4 (vwap_pullback, src=futures_proxy) params={"structure_break_persistence_seconds": 120.0}
[2026-10-03T08:16:42Z] [r33_VWAP] VWAP_Base_Test4 OK (12239s, 19854 trades, 61G free)
[2026-10-03T08:16:42Z] [r33_VWAP] ==========================================
[2026-10-03T08:16:42Z] [r33_VWAP] sweep [r33_VWAP] COMPLETE -> data/historical/backtest_reports/s6_r33_VWAP (736min)
[2026-10-03T08:16:42Z] [r33_VWAP] ==========================================
== finished configs (all chains): 523
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r31_chain.heartbeat ended without a finish line (last: 2026-10-03 01:10 IST r31_VWAP: complete; outputs in backtest_reports/s6_r31_VWAP (heartbeat/log files above carry the tag r31))
```
