# btsync status  2026-09-30T14:24:51Z UTC / 2026-09-30 19:54:51 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 19:54:51 IST / 14:24:51 UTC  load: 0.03 0.01 0.09  free: 8G avail  disk: 62G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- vwap_sep_chain.heartbeat
2026-09-30 18:55:06 IST vwap_sep: r29 done (rc=0)
2026-09-30 18:55:06 IST vwap_sep: start r30 (VWAP_PCR_Live_Convic)
2026-09-30 18:57:18 IST vwap_sep: r30 done (rc=0)
2026-09-30 18:57:19 IST vwap_sep: comparisons written
2026-09-30 18:57:19 IST vwap_sep: reaper timer restarted
2026-09-30 18:57:19 IST vwap_sep: chain finished
-- r30_chain.heartbeat
2026-09-30 18:55:06 IST r30: reaper timer stopped
2026-09-30 18:55:07 IST r30: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 18:57:18 IST r30: sweep finished rc=0
2026-09-30 18:57:18 IST r30: chain finished
-- r29_chain.heartbeat
2026-09-30 18:52:52 IST r29: reaper timer stopped
2026-09-30 18:52:54 IST r29: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 18:55:06 IST r29: sweep finished rc=0
2026-09-30 18:55:06 IST r29: chain finished
== last 8 s6_status lines:
[2026-09-30T13:25:07Z] [r30] ==========================================
[2026-09-30T13:25:07Z] [r30] sweep [r30] -> data/historical/backtest_reports/s6_r30 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T13:25:07Z] [r30] ==========================================
[2026-09-30T13:25:07Z] [r30] --- VWAP_PCR_Live_Convic (vwap_pullback_conviction, src=futures_proxy) params={"trail_min_buffer_pct": 0.015, "pcr_directional_ce_min": 1.1, "pcr_directional_pe_max": 1.0,
[2026-09-30T13:27:18Z] [r30] VWAP_PCR_Live_Convic OK (131s, 203 trades, 62G free)
[2026-09-30T13:27:18Z] [r30] ==========================================
[2026-09-30T13:27:18Z] [r30] sweep [r30] COMPLETE -> data/historical/backtest_reports/s6_r30 (2min)
[2026-09-30T13:27:18Z] [r30] ==========================================
== finished configs (all chains): 508
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
