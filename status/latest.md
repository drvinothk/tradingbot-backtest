# btsync status  2026-09-27T20:04:31Z UTC / 2026-09-28 01:34:31 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 01:34:31 IST / 20:04:31 UTC  load: 0.01 0.17 0.31  free: 8G avail  disk: 74G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- w14_chain.heartbeat
2026-09-27 17:18:33 IST w14: reaper timer stopped
2026-09-27 17:18:33 IST w14: frozen md5s: 6a26192c 587fefca 69ce1dd9 0bb606be cdec5753 dd220499 
2026-09-27 17:18:33 IST w14: chunk w14a: launching sweep_configs/renko14a_combo_batch.txt (4 configs, avg 4200s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-27 22:15:21 IST w14: chunk w14a: rc=0 17808s ok=4 shard-failures=0 tracebacks=0
2026-09-27 22:15:21 IST w14: chain finished (4 configs run)
2026-09-27 22:15:21 IST w14: reaper timer restarted
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
== last 8 s6_status lines:
[2026-09-27T19:00:56Z] [r15] s1_atr2 OK (171s, 9 trades, 74G free)
[2026-09-27T19:00:56Z] [r15] --- s1_atr25 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "atr_lookback_days": 2.5, "confirm_bricks":
[2026-09-27T19:03:45Z] [r15] s1_atr25 OK (169s, 9 trades, 74G free)
[2026-09-27T19:03:45Z] [r15] --- s1_atr3 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "atr_lookback_days": 3, "confirm_bricks": 2,
[2026-09-27T19:06:36Z] [r15] s1_atr3 OK (171s, 9 trades, 74G free)
[2026-09-27T19:06:36Z] [r15] ==========================================
[2026-09-27T19:06:36Z] [r15] sweep [r15] COMPLETE -> data/historical/backtest_reports/s6_r15 (8min)
[2026-09-27T19:06:36Z] [r15] ==========================================
== finished configs (all chains): 496
== md5:
94f7351d backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
