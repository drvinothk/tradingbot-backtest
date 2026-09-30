# btsync status  2026-09-30T04:33:33Z UTC / 2026-09-30 10:03:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 10:03:33 IST / 04:33:33 UTC  load: 0.13 0.21 0.26  free: 9G avail  disk: 64G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- q5floor_chain.heartbeat
2026-09-30 03:14:51 IST q5floor: start r22 (EMA_Convic_Paper_Q5Floor)
2026-09-30 06:04:08 IST q5floor: r22 done (rc=0)
2026-09-30 06:04:08 IST q5floor: start r23 (EMA_PCR_Live_Convic_Q5Floor)
2026-09-30 08:50:44 IST q5floor: r23 done (rc=0)
2026-09-30 08:50:44 IST q5floor: reaper timer restarted
2026-09-30 08:50:44 IST q5floor: chain finished
-- r23_chain.heartbeat
2026-09-30 06:04:08 IST r23: reaper timer stopped
2026-09-30 06:04:10 IST r23: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 08:50:44 IST r23: sweep finished rc=0
2026-09-30 08:50:44 IST r23: chain finished
-- r22_chain.heartbeat
2026-09-30 03:14:51 IST r22: reaper timer stopped
2026-09-30 03:14:53 IST r22: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 06:04:08 IST r22: sweep finished rc=0
2026-09-30 06:04:08 IST r22: chain finished
== last 8 s6_status lines:
[2026-09-30T00:34:10Z] [r23] ==========================================
[2026-09-30T00:34:10Z] [r23] sweep [r23] -> data/historical/backtest_reports/s6_r23 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T00:34:10Z] [r23] ==========================================
[2026-09-30T00:34:10Z] [r23] --- EMA_PCR_Live_Convic_Q5Floor (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buf
[2026-09-30T03:20:44Z] [r23] EMA_PCR_Live_Convic_Q5Floor OK (9994s, 690 trades, 63G free)
[2026-09-30T03:20:44Z] [r23] ==========================================
[2026-09-30T03:20:44Z] [r23] sweep [r23] COMPLETE -> data/historical/backtest_reports/s6_r23 (166min)
[2026-09-30T03:20:44Z] [r23] ==========================================
== finished configs (all chains): 504
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
