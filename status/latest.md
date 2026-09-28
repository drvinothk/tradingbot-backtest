# btsync status  2026-09-28T17:02:09Z UTC / 2026-09-28 22:32:09 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 22:32:09 IST / 17:02:09 UTC  load: 4.77 4.80 4.55  free: 6G avail  disk: 65G free
== units:
  backtest-20260928-162023.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ema_variants.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r18_chain.heartbeat
2026-09-28 21:50:24 IST r18: reaper timer stopped
2026-09-28 21:50:25 IST r18: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- ema_chain.heartbeat
2026-09-28 21:50:23 IST ema_chain: reaper timer stopped for the whole chain
2026-09-28 21:50:23 IST ema_chain: start r18 EMA_Convic_Paper (1,636 pairs)
-- p19_chain.heartbeat
2026-09-28 21:48:17 IST p19: reaper timer stopped
2026-09-28 21:48:18 IST p19: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 21:50:16 IST p19: sweep finished rc=0
2026-09-28 21:50:16 IST p19: chain finished
2026-09-28 21:50:16 IST p19: reaper timer restarted
== last 8 s6_status lines:
[2026-09-28T16:20:16Z] [p19] EMA_PCR_Live_Convic OK (118s, 56 trades, 65G free)
[2026-09-28T16:20:16Z] [p19] ==========================================
[2026-09-28T16:20:16Z] [p19] sweep [p19] COMPLETE -> data/historical/backtest_reports/s6_p19 (1min)
[2026-09-28T16:20:16Z] [p19] ==========================================
[2026-09-28T16:20:25Z] [r18] ==========================================
[2026-09-28T16:20:25Z] [r18] sweep [r18] -> data/historical/backtest_reports/s6_r18 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T16:20:25Z] [r18] ==========================================
[2026-09-28T16:20:25Z] [r18] --- EMA_Convic_Paper (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "require_atr_expansion": 
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
