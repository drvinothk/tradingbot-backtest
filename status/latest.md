# btsync status  2026-09-29T12:03:23Z UTC / 2026-09-29 17:33:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-29 17:33:23 IST / 12:03:23 UTC  load: 4.67 4.73 4.75  free: 6G avail  disk: 63G free
== units:
  backtest-20260929-070157.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_r20_notrail.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r20_chain.heartbeat
2026-09-29 15:31:18 IST r20: reaper timer stopped
2026-09-29 15:31:20 IST r20: QC ok; 1470 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- ema_chain.heartbeat
2026-09-29 00:53:50 IST ema_chain: start r19 EMA_PCR_Live_Convic (1,471 pairs from 2020-09-01)
2026-09-29 03:30:45 IST ema_chain: r19 done (rc=0)
2026-09-29 03:30:47 IST ema_chain: variant comparison written
2026-09-29 03:30:47 IST ema_chain: live/paper comparisons written
2026-09-29 03:30:47 IST ema_chain: reaper timer restarted
2026-09-29 03:30:47 IST ema_chain: chain finished
-- r19_chain.heartbeat
2026-09-29 00:53:50 IST r19: reaper timer stopped
2026-09-29 00:53:52 IST r19: QC ok; 1470 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-29 03:30:45 IST r19: sweep finished rc=0
2026-09-29 03:30:45 IST r19: chain finished
== last 8 s6_status lines:
[2026-09-28T22:00:45Z] [r19] EMA_PCR_Live_Convic OK (9413s, 3381 trades, 65G free)
[2026-09-28T22:00:45Z] [r19] ==========================================
[2026-09-28T22:00:45Z] [r19] sweep [r19] COMPLETE -> data/historical/backtest_reports/s6_r19 (156min)
[2026-09-28T22:00:45Z] [r19] ==========================================
[2026-09-29T10:01:20Z] [r20] ==========================================
[2026-09-29T10:01:20Z] [r20] sweep [r20] -> data/historical/backtest_reports/s6_r20 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-29T10:01:20Z] [r20] ==========================================
[2026-09-29T10:01:20Z] [r20] --- EMA_PCR_Live_Convic_NoTrail (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buf
== finished configs (all chains): 500
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-09-28T12:22:01Z] [r17] *** EMA_Base merge FAILED
[2026-09-28T12:22:01Z] [r17] EMA_Base HAD SHARD FAILURES (13s, 0 trades, 65G free)
```
