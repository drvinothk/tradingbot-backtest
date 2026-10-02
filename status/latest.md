# btsync status  2026-10-02T19:21:54Z UTC / 2026-10-03 00:51:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 00:51:54 IST / 19:21:54 UTC  load: 4.55 4.34 3.00  free: 8G avail  disk: 61G free
== units:
  backtest-20261002-190632.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./launch_config_run.sh r31 sweep_configs/vwa
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r31_chain.heartbeat
2026-10-01 13:43:52 IST r31: reaper timer stopped
2026-10-01 13:43:54 IST r31: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-10-01 17:15:47 IST r31: sweep finished rc=0
2026-10-01 17:15:47 IST r31: chain finished
2026-10-03 00:36:32 IST r31: reaper timer stopped
2026-10-03 00:36:34 IST r31: QC ok; 70 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 53208abd
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
[2026-10-02T19:06:34Z] [r31] ==========================================
[2026-10-02T19:06:34Z] [r31] sweep [r31] -> data/historical/backtest_reports/s6_r31 (4 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-02T19:06:34Z] [r31] ==========================================
[2026-10-02T19:06:34Z] [r31] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, "trail_acti
[2026-10-02T19:13:59Z] [r31] VWAP_Base OK (445s, 996 trades, 61G free)
[2026-10-02T19:13:59Z] [r31] --- VWAP_PCR_Live_Convic (vwap_pullback_conviction, src=futures_proxy) params={"trail_min_buffer_pct": 0.015, "pcr_directional_ce_min": 1.1, "pcr_directional_pe_max": 1.0,
[2026-10-02T19:21:08Z] [r31] VWAP_PCR_Live_Convic OK (429s, 633 trades, 61G free)
[2026-10-02T19:21:08Z] [r31] --- VWAP_Conviction (vwap_pullback_conviction, src=futures_proxy) params={"exit_legs": [{"kind": "core", "stop_pct": 0.08, "qty_fraction": 0.4, "use_structure": true, "tra
== finished configs (all chains): 521
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
