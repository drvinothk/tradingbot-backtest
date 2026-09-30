# btsync status  2026-09-30T11:31:54Z UTC / 2026-09-30 17:01:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 17:01:54 IST / 11:31:54 UTC  load: 4.75 4.71 4.73  free: 6G avail  disk: 62G free
== units:
  backtest-20260930-061007.service loaded active running /bin/bash ./chain_final_select.sh
  backtest-20260930-100731.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_vwap_sep.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r28_chain.heartbeat
2026-09-30 16:00:00 IST r28: reaper timer stopped
2026-09-30 16:00:02 IST r28: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- final_select_chain.heartbeat
2026-09-30 11:40:07 IST final_select: reaper timer stopped for the whole chain
2026-09-30 11:40:07 IST final_select: start r27 (EMA_Base_Q5Floor_TSL)
2026-09-30 16:00:00 IST final_select: r27 done (rc=0)
2026-09-30 16:00:00 IST final_select: start r28 (EMA_Convic_Paper_Q5Floor_1p1)
-- r27_chain.heartbeat
2026-09-30 11:40:07 IST r27: reaper timer stopped
2026-09-30 11:40:08 IST r27: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 16:00:00 IST r27: sweep finished rc=0
2026-09-30 16:00:00 IST r27: chain finished
== last 8 s6_status lines:
[2026-09-30T10:30:00Z] [r27] EMA_Base_Q5Floor_TSL OK (15592s, 4022 trades, 62G free)
[2026-09-30T10:30:00Z] [r27] ==========================================
[2026-09-30T10:30:00Z] [r27] sweep [r27] COMPLETE -> data/historical/backtest_reports/s6_r27 (259min)
[2026-09-30T10:30:00Z] [r27] ==========================================
[2026-09-30T10:30:02Z] [r28] ==========================================
[2026-09-30T10:30:02Z] [r28] sweep [r28] -> data/historical/backtest_reports/s6_r28 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T10:30:02Z] [r28] ==========================================
[2026-09-30T10:30:02Z] [r28] --- EMA_Convic_Paper_Q5Floor_1p1 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activa
== finished configs (all chains): 505
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
