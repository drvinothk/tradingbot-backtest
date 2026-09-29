# btsync status  2026-09-29T16:55:53Z UTC / 2026-09-29 22:25:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-29 22:25:53 IST / 16:55:53 UTC  load: 0.10 0.16 0.18  free: 8G avail  disk: 63G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r20_chain.heartbeat
2026-09-29 15:31:18 IST r20: reaper timer stopped
2026-09-29 15:31:20 IST r20: QC ok; 1470 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-29 18:06:53 IST r20: sweep finished rc=0
2026-09-29 18:06:53 IST r20: chain finished
2026-09-29 18:06:53 IST r20: reaper timer restarted
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
[2026-09-29T10:01:20Z] [r20] ==========================================
[2026-09-29T10:01:20Z] [r20] sweep [r20] -> data/historical/backtest_reports/s6_r20 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-29T10:01:20Z] [r20] ==========================================
[2026-09-29T10:01:20Z] [r20] --- EMA_PCR_Live_Convic_NoTrail (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buf
[2026-09-29T12:36:53Z] [r20] EMA_PCR_Live_Convic_NoTrail OK (9333s, 3001 trades, 63G free)
[2026-09-29T12:36:53Z] [r20] ==========================================
[2026-09-29T12:36:53Z] [r20] sweep [r20] COMPLETE -> data/historical/backtest_reports/s6_r20 (155min)
[2026-09-29T12:36:53Z] [r20] ==========================================
== finished configs (all chains): 501
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
