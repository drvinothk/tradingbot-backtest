# btsync status  2026-09-30T03:12:07Z UTC / 2026-09-30 08:42:07 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 08:42:07 IST / 03:12:07 UTC  load: 5.23 4.88 4.76  free: 7G avail  disk: 63G free
== units:
  backtest-20260929-184442.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_q5floor.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r23_chain.heartbeat
2026-09-30 06:04:08 IST r23: reaper timer stopped
2026-09-30 06:04:10 IST r23: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- q5floor_chain.heartbeat
2026-09-30 00:14:42 IST q5floor: reaper timer stopped for the whole chain
2026-09-30 00:14:42 IST q5floor: start r21 (EMA_Base_Q5Floor)
2026-09-30 03:14:51 IST q5floor: r21 done (rc=0)
2026-09-30 03:14:51 IST q5floor: start r22 (EMA_Convic_Paper_Q5Floor)
2026-09-30 06:04:08 IST q5floor: r22 done (rc=0)
2026-09-30 06:04:08 IST q5floor: start r23 (EMA_PCR_Live_Convic_Q5Floor)
-- r22_chain.heartbeat
2026-09-30 03:14:51 IST r22: reaper timer stopped
2026-09-30 03:14:53 IST r22: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-30 06:04:08 IST r22: sweep finished rc=0
2026-09-30 06:04:08 IST r22: chain finished
== last 8 s6_status lines:
[2026-09-30T00:34:08Z] [r22] EMA_Convic_Paper_Q5Floor OK (10155s, 1158 trades, 63G free)
[2026-09-30T00:34:08Z] [r22] ==========================================
[2026-09-30T00:34:08Z] [r22] sweep [r22] COMPLETE -> data/historical/backtest_reports/s6_r22 (169min)
[2026-09-30T00:34:08Z] [r22] ==========================================
[2026-09-30T00:34:10Z] [r23] ==========================================
[2026-09-30T00:34:10Z] [r23] sweep [r23] -> data/historical/backtest_reports/s6_r23 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T00:34:10Z] [r23] ==========================================
[2026-09-30T00:34:10Z] [r23] --- EMA_PCR_Live_Convic_Q5Floor (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buf
== finished configs (all chains): 503
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9478s ago (>2.5h) while a unit is running -- possible stall
```
