# btsync status  2026-09-27T19:03:23Z UTC / 2026-09-28 00:33:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 00:33:24 IST / 19:03:24 UTC  load: 4.38 2.93 1.31  free: 7G avail  disk: 74G free
== units:
  backtest-20260927-185805.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && sudo -n systemctl stop backtest-reaper.timer
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
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
[2026-09-27T16:45:21Z] [w14a] sweep [w14a] COMPLETE -> data/historical/backtest_reports/s6_w14a (296min)
[2026-09-27T16:45:21Z] [w14a] ==========================================
[2026-09-27T18:58:05Z] [r15] ==========================================
[2026-09-27T18:58:05Z] [r15] sweep [r15] -> data/historical/backtest_reports/s6_r15 (3 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-27T18:58:05Z] [r15] ==========================================
[2026-09-27T18:58:05Z] [r15] --- s1_atr2 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "atr_lookback_days": 2, "confirm_bricks": 2,
[2026-09-27T19:00:56Z] [r15] s1_atr2 OK (171s, 9 trades, 74G free)
[2026-09-27T19:00:56Z] [r15] --- s1_atr25 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 1.0, "atr_lookback_days": 2.5, "confirm_bricks":
== finished configs (all chains): 494
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
