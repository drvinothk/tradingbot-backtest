# btsync status  2026-09-30T15:56:40Z UTC / 2026-09-30 21:26:40 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 21:26:40 IST / 15:56:40 UTC  load: 4.72 4.77 4.74  free: 6G avail  disk: 62G free
== units:
  backtest-20260930-143356.service loaded active running /bin/bash ./chain_final_select2.sh
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r24_chain.heartbeat
2026-09-30 10:46:19 IST r24: reaper timer stopped
2026-09-30 10:46:20 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 20:03:56 IST r24: reaper timer stopped
2026-09-30 20:03:57 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select2_chain.heartbeat
2026-09-30 20:03:56 IST final_select2: reaper timer stopped for the whole chain
2026-09-30 20:03:56 IST final_select2: start r24 (EMA_Convic_Paper_ATRonly)
-- vwap_sep_chain.heartbeat
2026-09-30 18:55:06 IST vwap_sep: r29 done (rc=0)
2026-09-30 18:55:06 IST vwap_sep: start r30 (VWAP_PCR_Live_Convic)
2026-09-30 18:57:18 IST vwap_sep: r30 done (rc=0)
2026-09-30 18:57:19 IST vwap_sep: comparisons written
2026-09-30 18:57:19 IST vwap_sep: reaper timer restarted
2026-09-30 18:57:19 IST vwap_sep: chain finished
== last 8 s6_status lines:
[2026-09-30T13:27:18Z] [r30] VWAP_PCR_Live_Convic OK (131s, 203 trades, 62G free)
[2026-09-30T13:27:18Z] [r30] ==========================================
[2026-09-30T13:27:18Z] [r30] sweep [r30] COMPLETE -> data/historical/backtest_reports/s6_r30 (2min)
[2026-09-30T13:27:18Z] [r30] ==========================================
[2026-09-30T14:33:57Z] [r24] ==========================================
[2026-09-30T14:33:57Z] [r24] sweep [r24] -> data/historical/backtest_reports/s6_r24 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T14:33:57Z] [r24] ==========================================
[2026-09-30T14:33:58Z] [r24] --- EMA_Convic_Paper_ATRonly (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 508
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
