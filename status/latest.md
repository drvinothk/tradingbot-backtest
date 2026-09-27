# btsync status  2026-09-27T09:24:40Z UTC / 2026-09-27 14:54:40 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-27 14:54:40 IST / 09:24:40 UTC  load: 0.00 0.09 1.18  free: 8G avail  disk: 74G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- w13_chain.heartbeat
2026-09-26 20:58:07 IST w13: chunk w13c: launching sweep_configs/renko12c_warm_batch.txt (6 configs, avg 3167s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-27 01:57:08 IST w13: chunk w13c: rc=0 17941s ok=6 shard-failures=0 tracebacks=0
2026-09-27 01:57:08 IST w13: chunk w13d: launching sweep_configs/renko12d_warm_batch.txt (10 configs, avg 3091s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-27 14:35:44 IST w13: chunk w13d: rc=0 45516s ok=10 shard-failures=0 tracebacks=0
2026-09-27 14:35:44 IST w13: chain finished (24 configs run)
2026-09-27 14:35:44 IST w13: reaper timer restarted
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
[2026-09-27T06:05:17Z] [w13d] w12_pd3_e4 OK (5451s, 356 trades, 74G free)
[2026-09-27T06:05:17Z] [w13d] --- w12_pd4_tf5x5 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 5, "direction_filt
[2026-09-27T07:34:33Z] [w13d] w12_pd4_tf5x5 OK (5356s, 435 trades, 74G free)
[2026-09-27T07:34:33Z] [w13d] --- w12_pd5_b833mv50 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 15, "direction_
[2026-09-27T09:05:44Z] [w13d] w12_pd5_b833mv50 OK (5471s, 208 trades, 74G free)
[2026-09-27T09:05:44Z] [w13d] ==========================================
[2026-09-27T09:05:44Z] [w13d] sweep [w13d] COMPLETE -> data/historical/backtest_reports/s6_w13d (758min)
[2026-09-27T09:05:44Z] [w13d] ==========================================
== finished configs (all chains): 489
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
