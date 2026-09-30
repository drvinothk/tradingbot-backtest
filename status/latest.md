# btsync status  2026-09-30T05:17:09Z UTC / 2026-09-30 10:47:09 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 10:47:09 IST / 05:17:09 UTC  load: 2.89 1.08 0.61  free: 8G avail  disk: 63G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r24_chain.heartbeat
2026-09-30 10:46:19 IST r24: reaper timer stopped
2026-09-30 10:46:20 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- gatemix_chain.heartbeat
2026-09-30 10:46:19 IST gatemix: reaper timer stopped for the whole chain
2026-09-30 10:46:19 IST gatemix: start r24 (EMA_Convic_Paper_ATRonly)
-- q5floor_chain.heartbeat
2026-09-30 03:14:51 IST q5floor: start r22 (EMA_Convic_Paper_Q5Floor)
2026-09-30 06:04:08 IST q5floor: r22 done (rc=0)
2026-09-30 06:04:08 IST q5floor: start r23 (EMA_PCR_Live_Convic_Q5Floor)
2026-09-30 08:50:44 IST q5floor: r23 done (rc=0)
2026-09-30 08:50:44 IST q5floor: reaper timer restarted
2026-09-30 08:50:44 IST q5floor: chain finished
== last 8 s6_status lines:
[2026-09-30T03:20:44Z] [r23] EMA_PCR_Live_Convic_Q5Floor OK (9994s, 690 trades, 63G free)
[2026-09-30T03:20:44Z] [r23] ==========================================
[2026-09-30T03:20:44Z] [r23] sweep [r23] COMPLETE -> data/historical/backtest_reports/s6_r23 (166min)
[2026-09-30T03:20:44Z] [r23] ==========================================
[2026-09-30T05:16:20Z] [r24] ==========================================
[2026-09-30T05:16:20Z] [r24] sweep [r24] -> data/historical/backtest_reports/s6_r24 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T05:16:20Z] [r24] ==========================================
[2026-09-30T05:16:20Z] [r24] --- EMA_Convic_Paper_ATRonly (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation
== finished configs (all chains): 504
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r24_chain.heartbeat ended without a finish line (last: 2026-09-30 10:46:20 IST r24: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd)
! chain gatemix_chain.heartbeat ended without a finish line (last: 2026-09-30 10:46:19 IST gatemix: start r24 (EMA_Convic_Paper_ATRonly))
```
