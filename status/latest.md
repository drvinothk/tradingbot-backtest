# btsync status  2026-10-02T19:36:08Z UTC / 2026-10-03 01:06:08 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 01:06:08 IST / 19:36:08 UTC  load: 2.46 4.09 3.86  free: 9G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r31_chain.heartbeat
2026-10-03 00:36:32 IST r31: reaper timer stopped
2026-10-03 00:36:34 IST r31: QC ok; 70 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-03 01:05:32 IST r31: sweep finished rc=0
2026-10-03 01:05:32 IST r31: chain finished
2026-10-03 01:05:32 IST r31: reaper timer restarted
2026-10-03 01:10 IST r31_VWAP: complete; outputs in backtest_reports/s6_r31_VWAP (heartbeat/log files above carry the tag r31)
-- r39_chain.heartbeat
2026-10-02 20:59:10 IST r39: reaper timer stopped
2026-10-02 20:59:12 IST r39: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 23:50:05 IST r39: sweep finished rc=0
2026-10-02 23:50:05 IST r39: chain finished
2026-10-02 23:50:05 IST r39: reaper timer restarted
-- r38_chain.heartbeat
2026-10-02 13:21:20 IST r38: reaper timer stopped
2026-10-02 13:21:21 IST r38: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-02 16:17:46 IST r38: sweep finished rc=0
2026-10-02 16:17:46 IST r38: chain finished
2026-10-02 16:17:46 IST r38: reaper timer restarted
== last 8 s6_status lines:
[2026-10-02T19:21:08Z] [r31] VWAP_PCR_Live_Convic OK (429s, 633 trades, 61G free)
[2026-10-02T19:21:08Z] [r31] --- VWAP_Conviction (vwap_pullback_conviction, src=futures_proxy) params={"exit_legs": [{"kind": "core", "stop_pct": 0.08, "qty_fraction": 0.4, "use_structure": true, "tra
[2026-10-02T19:28:07Z] [r31] VWAP_Conviction OK (419s, 462 trades, 61G free)
[2026-10-02T19:28:07Z] [r31] --- VWAP_Base_Test4 (vwap_pullback, src=futures_proxy) params={"structure_break_persistence_seconds": 120.0}
[2026-10-02T19:35:32Z] [r31] VWAP_Base_Test4 OK (445s, 1009 trades, 61G free)
[2026-10-02T19:35:32Z] [r31] ==========================================
[2026-10-02T19:35:32Z] [r31] sweep [r31] COMPLETE -> data/historical/backtest_reports/s6_r31 (28min)
[2026-10-02T19:35:32Z] [r31] ==========================================
== finished configs (all chains): 523
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r31_chain.heartbeat ended without a finish line (last: 2026-10-03 01:10 IST r31_VWAP: complete; outputs in backtest_reports/s6_r31_VWAP (heartbeat/log files above carry the tag r31))
```
