# btsync status  2026-10-02T23:31:29Z UTC / 2026-10-03 05:01:29 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 05:01:29 IST / 23:31:29 UTC  load: 4.66 4.66 4.65  free: 7G avail  disk: 61G free
== units:
  backtest-20261002-195957.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./launch_config_run_optvol.sh r33_VWAP sweep
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r33_VWAP_chain.heartbeat
2026-10-03 01:29:57 IST r33_VWAP: reaper timer stopped
2026-10-03 01:29:58 IST r33_VWAP: QC ok; 1472 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine 53208abd
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
[2026-10-02T19:59:43Z] [r32_VWAP] sweep [r32_VWAP] COMPLETE -> data/historical/backtest_reports/s6_r32_VWAP (15min)
[2026-10-02T19:59:43Z] [r32_VWAP] ==========================================
[2026-10-02T19:59:58Z] [r33_VWAP] ==========================================
[2026-10-02T19:59:58Z] [r33_VWAP] sweep [r33_VWAP] -> data/historical/backtest_reports/s6_r33_VWAP (4 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-02T19:59:58Z] [r33_VWAP] ==========================================
[2026-10-02T19:59:58Z] [r33_VWAP] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, "trail
[2026-10-02T23:02:33Z] [r33_VWAP] VWAP_Base OK (10954s, 19613 trades, 61G free)
[2026-10-02T23:02:33Z] [r33_VWAP] --- VWAP_PCR_Live_Convic (vwap_pullback_conviction, src=futures_proxy) params={"trail_min_buffer_pct": 0.015, "pcr_directional_ce_min": 1.1, "pcr_directional_pe_max":
== finished configs (all chains): 523
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
