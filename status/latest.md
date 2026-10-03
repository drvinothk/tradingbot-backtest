# btsync status  2026-10-03T16:25:18Z UTC / 2026-10-03 21:55:18 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-03 21:55:18 IST / 16:25:18 UTC  load: 4.88 4.75 4.76  free: 6G avail  disk: 61G free
== units:
  backtest-20261003-102853.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_vwap_overlays.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r35_VWAP_ema30_chain.heartbeat
2026-10-03 19:07:26 IST r35_VWAP_ema30: reaper timer stopped
2026-10-03 19:07:28 IST r35_VWAP_ema30: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
-- vwap_overlays_chain.heartbeat
2026-10-03 15:58:53 IST vwap_overlays: reaper timer stopped
2026-10-03 15:58:53 IST vwap_overlays: start r34_VWAP_redbar (overlay redbar_zone_trend11) engine 1b5fd13a
2026-10-03 19:07:26 IST vwap_overlays: r34_VWAP_redbar done (rc=0)
2026-10-03 19:07:26 IST vwap_overlays: start r35_VWAP_ema30 (overlay ema30_aligned) engine 1b5fd13a
-- r34_VWAP_redbar_chain.heartbeat
2026-10-03 15:58:53 IST r34_VWAP_redbar: reaper timer stopped
2026-10-03 15:58:54 IST r34_VWAP_redbar: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 1b5fd13a
2026-10-03 19:07:26 IST r34_VWAP_redbar: sweep finished rc=0
2026-10-03 19:07:26 IST r34_VWAP_redbar: chain finished
== last 8 s6_status lines:
[2026-10-03T13:37:25Z] [r34_VWAP_redbar] VWAP_Base OK (11311s, 15699 trades, 61G free)
[2026-10-03T13:37:25Z] [r34_VWAP_redbar] ==========================================
[2026-10-03T13:37:25Z] [r34_VWAP_redbar] sweep [r34_VWAP_redbar] COMPLETE -> data/historical/backtest_reports/s6_r34_VWAP_redbar (188min)
[2026-10-03T13:37:25Z] [r34_VWAP_redbar] ==========================================
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] ==========================================
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] sweep [r35_VWAP_ema30] -> data/historical/backtest_reports/s6_r35_VWAP_ema30 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-d
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] ==========================================
[2026-10-03T13:37:28Z] [r35_VWAP_ema30] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, 
== finished configs (all chains): 523
== md5:
1b5fd13a backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 10071s ago (>2.5h) while a unit is running -- possible stall
```
