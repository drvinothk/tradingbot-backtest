# btsync status  2026-09-28T15:11:24Z UTC / 2026-09-28 20:41:24 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 20:41:24 IST / 15:11:24 UTC  load: 4.78 4.58 4.65  free: 6G avail  disk: 65G free
== units:
  backtest-20260928-122342.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./launch_config_run.sh r17 sweep_configs/ema
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r17_chain.heartbeat
2026-09-28 17:53:42 IST r17: reaper timer stopped
2026-09-28 17:53:44 IST r17: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
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
[2026-09-28T12:22:01Z] [r17] EMA_Base HAD SHARD FAILURES (13s, 0 trades, 65G free)
[2026-09-28T12:22:01Z] [r17] ==========================================
[2026-09-28T12:22:01Z] [r17] sweep [r17] COMPLETE -> data/historical/backtest_reports/s6_r17 (0min)
[2026-09-28T12:22:01Z] [r17] ==========================================
[2026-09-28T12:23:44Z] [r17] ==========================================
[2026-09-28T12:23:44Z] [r17] sweep [r17] -> data/historical/backtest_reports/s6_r17 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-28T12:23:44Z] [r17] ==========================================
[2026-09-28T12:23:44Z] [r17] --- EMA_Base (ema_micro_pullback, src=combined_2020) params={"structure_break_atr_multiplier": 0.6, "structure_break_persistence_seconds": 6}
== finished configs (all chains): 498
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-09-28T12:22:01Z] [r17] *** EMA_Base merge FAILED
[2026-09-28T12:22:01Z] [r17] EMA_Base HAD SHARD FAILURES (13s, 0 trades, 65G free)
! newest config started/finished 10060s ago (>2.5h) while a unit is running -- possible stall
```
