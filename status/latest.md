# btsync status  2026-09-28T12:20:31Z UTC / 2026-09-28 17:50:31 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 17:50:31 IST / 12:20:31 UTC  load: 0.84 1.08 0.52  free: 8G avail  disk: 65G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r17_chain.heartbeat
2026-09-28 17:50:08 IST r17: ABORT -- a sweep is running
-- r17p_chain.heartbeat
2026-09-28 17:47:08 IST r17p: reaper timer stopped
2026-09-28 17:47:09 IST r17p: QC ok; 17 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
2026-09-28 17:49:08 IST r17p: sweep finished rc=0
2026-09-28 17:49:08 IST r17p: chain finished
2026-09-28 17:49:08 IST r17p: reaper timer restarted
-- r16_chain.heartbeat
2026-09-28 02:51:20 IST r16: reaper timer stopped
2026-09-28 02:51:20 IST r16: launching full 2020-2025 sweep: full2020_base (1 config, 1393 day:expiry pairs, 2020-01-01..2025-08-21, source=combined_2020, --extra-warmup-days 12, multi-trade, SHARD_COUNT=4)
2026-09-28 12:34:47 IST r16: sweep finished rc=0
2026-09-28 12:34:47 IST r16: reaper timer restarted
2026-09-28 12:34:47 IST r16: chain finished
== last 8 s6_status lines:
[2026-09-28T12:17:09Z] [r17p] ==========================================
[2026-09-28T12:17:09Z] [r17p] sweep [r17p] -> data/historical/backtest_reports/s6_r17p (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T12:17:09Z] [r17p] ==========================================
[2026-09-28T12:17:09Z] [r17p] --- EMA_Base (ema_micro_pullback, src=combined_2020) params={"structure_break_atr_multiplier": 0.6, "structure_break_persistence_seconds": 6}
[2026-09-28T12:19:08Z] [r17p] EMA_Base OK (119s, 196 trades, 65G free)
[2026-09-28T12:19:08Z] [r17p] ==========================================
[2026-09-28T12:19:08Z] [r17p] sweep [r17p] COMPLETE -> data/historical/backtest_reports/s6_r17p (1min)
[2026-09-28T12:19:08Z] [r17p] ==========================================
== finished configs (all chains): 498
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain r17_chain.heartbeat ended without a finish line (last: 2026-09-28 17:50:08 IST r17: ABORT -- a sweep is running)
! r17_chain.heartbeat: 2026-09-28 17:50:08 IST r17: ABORT -- a sweep is running
```
