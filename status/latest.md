# btsync status  2026-09-29T21:44:03Z UTC / 2026-09-30 03:14:03 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 03:14:03 IST / 21:44:03 UTC  load: 4.84 4.89 4.88  free: 7G avail  disk: 63G free
== units:
  backtest-20260929-184442.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_q5floor.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r21_chain.heartbeat
2026-09-30 00:14:42 IST r21: reaper timer stopped
2026-09-30 00:14:44 IST r21: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- q5floor_chain.heartbeat
2026-09-30 00:14:42 IST q5floor: reaper timer stopped for the whole chain
2026-09-30 00:14:42 IST q5floor: start r21 (EMA_Base_Q5Floor)
-- r20_chain.heartbeat
2026-09-29 15:31:18 IST r20: reaper timer stopped
2026-09-29 15:31:20 IST r20: QC ok; 1470 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-29 18:06:53 IST r20: sweep finished rc=0
2026-09-29 18:06:53 IST r20: chain finished
2026-09-29 18:06:53 IST r20: reaper timer restarted
== last 8 s6_status lines:
[2026-09-29T12:36:53Z] [r20] EMA_PCR_Live_Convic_NoTrail OK (9333s, 3001 trades, 63G free)
[2026-09-29T12:36:53Z] [r20] ==========================================
[2026-09-29T12:36:53Z] [r20] sweep [r20] COMPLETE -> data/historical/backtest_reports/s6_r20 (155min)
[2026-09-29T12:36:53Z] [r20] ==========================================
[2026-09-29T18:44:44Z] [r21] ==========================================
[2026-09-29T18:44:44Z] [r21] sweep [r21] -> data/historical/backtest_reports/s6_r21 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-29T18:44:44Z] [r21] ==========================================
[2026-09-29T18:44:44Z] [r21] --- EMA_Base_Q5Floor (ema_micro_pullback_conviction, src=combined_2020) params={"min_ema_spread_atr_ratio": 1.042}
== finished configs (all chains): 501
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 10760s ago (>2.5h) while a unit is running -- possible stall
```
