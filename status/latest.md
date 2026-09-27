# btsync status  2026-09-27T16:04:44Z UTC / 2026-09-27 21:34:44 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-27 21:34:44 IST / 16:04:44 UTC  load: 4.24 4.33 4.29  free: 7G avail  disk: 74G free
== units:
  backtest-20260927-114833.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && TAG=w14 END_BY_UTC=\"2026-09-28 12:00:00\" S
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- w14_chain.heartbeat
2026-09-27 17:18:33 IST w14: reaper timer stopped
2026-09-27 17:18:33 IST w14: frozen md5s: 6a26192c 587fefca 69ce1dd9 0bb606be cdec5753 dd220499 
2026-09-27 17:18:33 IST w14: chunk w14a: launching sweep_configs/renko14a_combo_batch.txt (4 configs, avg 4200s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
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
[2026-09-27T11:48:37Z] [w14a] ==========================================
[2026-09-27T11:48:37Z] [w14a] --- w14_s1_pe_msd1 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "confirm_bricks": 2, "entry_mode": "
[2026-09-27T12:36:28Z] [w14a] w14_s1_pe_msd1 OK (2871s, 44 trades, 74G free)
[2026-09-27T12:36:28Z] [w14a] --- w14_s1_pe_exit_wide (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "confirm_bricks": 2, "entry_mod
[2026-09-27T13:24:43Z] [w14a] w14_s1_pe_exit_wide OK (2895s, 60 trades, 74G free)
[2026-09-27T13:24:43Z] [w14a] --- w14_base_pe_msd1_wide (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 5, "direct
[2026-09-27T15:04:01Z] [w14a] w14_base_pe_msd1_wide OK (5958s, 182 trades, 74G free)
[2026-09-27T15:04:01Z] [w14a] --- w14_mv50_pe_msd1 (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 6.25, "brick_source_timeframe_minutes": 15, "direction_
== finished configs (all chains): 492
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
