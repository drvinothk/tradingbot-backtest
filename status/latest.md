# btsync status  2026-09-29T09:20:33Z UTC / 2026-09-29 14:50:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-29 14:50:33 IST / 09:20:33 UTC  load: 0.52 0.58 0.46  free: 8G avail  disk: 64G free
== units:
  backtest-20260929-070157.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_r20_notrail.sh"
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
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
-- r18_chain.heartbeat
2026-09-28 21:50:24 IST r18: reaper timer stopped
2026-09-28 21:50:25 IST r18: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-29 00:53:50 IST r18: sweep finished rc=0
2026-09-29 00:53:50 IST r18: chain finished
== last 8 s6_status lines:
[2026-09-28T19:23:52Z] [r19] ==========================================
[2026-09-28T19:23:52Z] [r19] sweep [r19] -> data/historical/backtest_reports/s6_r19 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T19:23:52Z] [r19] ==========================================
[2026-09-28T19:23:52Z] [r19] --- EMA_PCR_Live_Convic (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buffer_pct"
[2026-09-28T22:00:45Z] [r19] EMA_PCR_Live_Convic OK (9413s, 3381 trades, 65G free)
[2026-09-28T22:00:45Z] [r19] ==========================================
[2026-09-28T22:00:45Z] [r19] sweep [r19] COMPLETE -> data/historical/backtest_reports/s6_r19 (156min)
[2026-09-28T22:00:45Z] [r19] ==========================================
== finished configs (all chains): 500
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 40789s ago (>2.5h) while a unit is running -- possible stall
```
