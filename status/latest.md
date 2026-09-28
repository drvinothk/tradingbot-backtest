# btsync status  2026-09-28T21:26:52Z UTC / 2026-09-29 02:56:52 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-29 02:56:52 IST / 21:26:52 UTC  load: 5.14 4.83 4.76  free: 8G avail  disk: 65G free
== units:
  backtest-20260928-162023.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ema_variants.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r19_chain.heartbeat
2026-09-29 00:53:50 IST r19: reaper timer stopped
2026-09-29 00:53:52 IST r19: QC ok; 1470 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- ema_chain.heartbeat
2026-09-28 21:50:23 IST ema_chain: reaper timer stopped for the whole chain
2026-09-28 21:50:23 IST ema_chain: start r18 EMA_Convic_Paper (1,636 pairs)
2026-09-29 00:53:50 IST ema_chain: r18 done (rc=0)
2026-09-29 00:53:50 IST ema_chain: start r19 EMA_PCR_Live_Convic (1,471 pairs from 2020-09-01)
-- r18_chain.heartbeat
2026-09-28 21:50:24 IST r18: reaper timer stopped
2026-09-28 21:50:25 IST r18: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-29 00:53:50 IST r18: sweep finished rc=0
2026-09-29 00:53:50 IST r18: chain finished
== last 8 s6_status lines:
[2026-09-28T19:23:49Z] [r18] EMA_Convic_Paper OK (11004s, 6569 trades, 65G free)
[2026-09-28T19:23:49Z] [r18] ==========================================
[2026-09-28T19:23:49Z] [r18] sweep [r18] COMPLETE -> data/historical/backtest_reports/s6_r18 (183min)
[2026-09-28T19:23:49Z] [r18] ==========================================
[2026-09-28T19:23:52Z] [r19] ==========================================
[2026-09-28T19:23:52Z] [r19] sweep [r19] -> data/historical/backtest_reports/s6_r19 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T19:23:52Z] [r19] ==========================================
[2026-09-28T19:23:52Z] [r19] --- EMA_PCR_Live_Convic (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_min_buffer_pct"
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
