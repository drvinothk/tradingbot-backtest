# btsync status  2026-10-03T16:42:33Z UTC / 2026-10-03 22:12:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 22:12:33 IST / 16:42:33 UTC  load: 0.03 1.32 3.14  free: 9G avail  disk: 61G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- vwap_overlays_chain.heartbeat
2026-10-03 15:58:53 IST vwap_overlays: start r34_VWAP_redbar (overlay redbar_zone_trend11) engine 1b5fd13a
2026-10-03 19:07:26 IST vwap_overlays: r34_VWAP_redbar done (rc=0)
2026-10-03 19:07:26 IST vwap_overlays: start r35_VWAP_ema30 (overlay ema30_aligned) engine 1b5fd13a
2026-10-03 22:06:21 IST vwap_overlays: r35_VWAP_ema30 done (rc=0)
2026-10-03 22:06:21 IST vwap_overlays: reaper timer restarted
2026-10-03 22:06:21 IST vwap_overlays: chain finished
-- r35_VWAP_ema30_chain.heartbeat
2026-10-03 19:07:26 IST r35_VWAP_ema30: reaper timer stopped
2026-10-03 19:07:28 IST r35_VWAP_ema30: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
2026-10-03 22:06:21 IST r35_VWAP_ema30: sweep finished rc=0
2026-10-03 22:06:21 IST r35_VWAP_ema30: chain finished
-- r34_VWAP_redbar_chain.heartbeat
2026-10-03 15:58:53 IST r34_VWAP_redbar: reaper timer stopped
2026-10-03 15:58:54 IST r34_VWAP_redbar: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
2026-10-03 19:07:26 IST r34_VWAP_redbar: sweep finished rc=0
2026-10-03 19:07:26 IST r34_VWAP_redbar: chain finished
== last 8 s6_status lines:
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] ==========================================
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] sweep [r35_VWAP_ema30] -> data/historical/backtest_reports/s6_r35_VWAP_ema30 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-d
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] ==========================================
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, 
[2026-10-03T16:36:21Z] [r35_VWAP_ema30] VWAP_Base OK (10733s, 14407 trades, 61G free)
[2026-10-03T16:36:21Z] [r35_VWAP_ema30] ==========================================
[2026-10-03T16:36:21Z] [r35_VWAP_ema30] sweep [r35_VWAP_ema30] COMPLETE -> data/historical/backtest_reports/s6_r35_VWAP_ema30 (178min)
[2026-10-03T16:36:21Z] [r35_VWAP_ema30] ==========================================
== finished configs (all chains): 523
== md5:
1b5fd13a backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: fflush failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
