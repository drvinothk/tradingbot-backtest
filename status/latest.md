# btsync status  2026-10-03T12:36:49Z UTC / 2026-10-03 18:06:49 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 18:06:49 IST / 12:36:49 UTC  load: 4.49 4.66 4.71  free: 8G avail  disk: 61G free
== units:
  backtest-20261003-102853.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_vwap_overlays.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r34_VWAP_redbar_chain.heartbeat
2026-10-03 15:58:53 IST r34_VWAP_redbar: reaper timer stopped
2026-10-03 15:58:54 IST r34_VWAP_redbar: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
-- vwap_overlays_chain.heartbeat
2026-10-03 15:58:53 IST vwap_overlays: reaper timer stopped
2026-10-03 15:58:53 IST vwap_overlays: start r34_VWAP_redbar (overlay redbar_zone_trend11) engine 1b5fd13a
-- qc_ovl_off_chain.heartbeat
2026-10-03 15:53:12 IST qc_ovl_off: reaper timer stopped
2026-10-03 15:53:13 IST qc_ovl_off: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
2026-10-03 15:55:07 IST qc_ovl_off: sweep finished rc=0
2026-10-03 15:55:07 IST qc_ovl_off: chain finished
2026-10-03 15:55:07 IST qc_ovl_off: reaper timer restarted
== last 8 s6_status lines:
[2026-10-03T10:25:06Z] [qc_ovl_off] VWAP_Base OK (113s, 226 trades, 61G free)
[2026-10-03T10:25:06Z] [qc_ovl_off] ==========================================
[2026-10-03T10:25:06Z] [qc_ovl_off] sweep [qc_ovl_off] COMPLETE -> data/historical/backtest_reports/s6_qc_ovl_off (1min)
[2026-10-03T10:25:06Z] [qc_ovl_off] ==========================================
[2026-10-03T10:28:54Z] [r34_VWAP_redbar] ==========================================
[2026-10-03T10:28:54Z] [r34_VWAP_redbar] sweep [r34_VWAP_redbar] -> data/historical/backtest_reports/s6_r34_VWAP_redbar (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmu
[2026-10-03T10:28:54Z] [r34_VWAP_redbar] ==========================================
[2026-10-03T10:28:54Z] [r34_VWAP_redbar] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5,
== finished configs (all chains): 523
== md5:
1b5fd13a backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
