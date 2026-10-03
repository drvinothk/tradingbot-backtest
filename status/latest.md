# btsync status  2026-10-03T10:21:54Z UTC / 2026-10-03 15:51:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 15:51:54 IST / 10:21:54 UTC  load: 2.37 0.62 0.20  free: 7G avail  disk: 61G free
== units:
  backtest-20261003-102113.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./run_qc_overlay.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qc_ovl_log_chain.heartbeat
2026-10-03 15:51:13 IST qc_ovl_log: reaper timer stopped
2026-10-03 15:51:15 IST qc_ovl_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
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
== last 8 s6_status lines:
[2026-10-03T08:16:42Z] [r33_VWAP] VWAP_Base_Test4 OK (12239s, 19854 trades, 61G free)
[2026-10-03T08:16:42Z] [r33_VWAP] ==========================================
[2026-10-03T08:16:42Z] [r33_VWAP] sweep [r33_VWAP] COMPLETE -> data/historical/backtest_reports/s6_r33_VWAP (736min)
[2026-10-03T08:16:42Z] [r33_VWAP] ==========================================
[2026-10-03T10:21:15Z] [qc_ovl_log] ==========================================
[2026-10-03T10:21:15Z] [qc_ovl_log] sweep [qc_ovl_log] -> data/historical/backtest_reports/s6_qc_ovl_log (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --dat
[2026-10-03T10:21:15Z] [qc_ovl_log] ==========================================
[2026-10-03T10:21:15Z] [qc_ovl_log] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, "tra
== finished configs (all chains): 523
== md5:
1b5fd13a backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
