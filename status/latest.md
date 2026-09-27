# btsync status  2026-09-27T05:20:40Z UTC / 2026-09-27 10:50:40 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-27 10:50:40 IST / 05:20:40 UTC  load: 4.24 4.26 4.26  free: 7G avail  disk: 74G free
== units:
  backtest-20260926-082551.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && TAG=w13 END_BY_UTC=\"2026-09-28 02:00:00\" S
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- w13_chain.heartbeat
2026-09-26 17:37:54 IST w13: chunk w13a: rc=0 13323s ok=4 shard-failures=0 tracebacks=0
2026-09-26 17:37:54 IST w13: chunk w13b: launching sweep_configs/renko12b_warm_batch.txt (4 configs, avg 3330s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-26 20:58:07 IST w13: chunk w13b: rc=0 12013s ok=4 shard-failures=0 tracebacks=0
2026-09-26 20:58:07 IST w13: chunk w13c: launching sweep_configs/renko12c_warm_batch.txt (6 configs, avg 3167s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-27 01:57:08 IST w13: chunk w13c: rc=0 17941s ok=6 shard-failures=0 tracebacks=0
2026-09-27 01:57:08 IST w13: chunk w13d: launching sweep_configs/renko12d_warm_batch.txt (10 configs, avg 3091s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
-- w12_chain.heartbeat
2026-09-26 11:38:28 IST w12: reaper timer stopped
2026-09-26 11:38:28 IST w12: frozen md5s: 587fefca 69ce1dd9 0bb606be cdec5753 dd220499 
2026-09-26 11:38:28 IST w12: chunk w12: launching sweep_configs/renko11_pilot.txt (1 configs, avg 4200s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 21')
2026-09-26 13:55:16 IST w12: chunk w12: rc=0 8208s ok=1 shard-failures=0 tracebacks=0
2026-09-26 13:55:16 IST w12: chunk w12a: launching sweep_configs/renko12a_warm_batch.txt (4 configs, avg 8208s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 21')
2026-09-26 13:55:34 IST w12: reaper timer restarted
-- mt1_chain.heartbeat
2026-09-26 01:10:21 IST mt1: reaper timer stopped
2026-09-26 01:10:21 IST mt1: launching renko10 multi-trade per-day (6 configs, SHARD_COUNT=4)
2026-09-26 06:27:30 IST mt1: batch finished rc=0 -- 6 OK (cumulative), 0 with failures
2026-09-26 06:27:30 IST mt1: reaper timer restarted
== last 8 s6_status lines:
[2026-09-27T02:02:40Z] [w13d] w12_h2_15m_fib_ema15 OK (2925s, 156 trades, 75G free)
[2026-09-27T02:02:40Z] [w13d] --- w12_h1_15m_fib_mv50 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 15, "directi
[2026-09-27T02:53:27Z] [w13d] w12_h1_15m_fib_mv50 OK (3047s, 201 trades, 74G free)
[2026-09-27T02:53:27Z] [w13d] --- w12_h6_5m_fib_cc5 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 5, "direction_
[2026-09-27T03:44:11Z] [w13d] w12_h6_5m_fib_cc5 OK (3044s, 253 trades, 74G free)
[2026-09-27T03:44:11Z] [w13d] --- w12_h4_15m_fib_nocap (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 15, "direct
[2026-09-27T04:34:26Z] [w13d] w12_h4_15m_fib_nocap OK (3015s, 299 trades, 74G free)
[2026-09-27T04:34:26Z] [w13d] --- w12_pd3_e4 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 10.0, "brick_source_timeframe_minutes": 5, "direction_filter_
== finished configs (all chains): 486
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
