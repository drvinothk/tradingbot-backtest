# btsync status  2026-09-28T12:11:52Z UTC / 2026-09-28 17:41:52 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-28 17:41:52 IST / 12:11:52 UTC  load: 0.02 0.01 0.05  free: 8G avail  disk: 65G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- r16_chain.heartbeat
2026-09-28 02:51:20 IST r16: reaper timer stopped
2026-09-28 02:51:20 IST r16: launching full 2020-2025 sweep: full2020_base (1 config, 1393 day:expiry pairs, 2020-01-01..2025-08-21, source=combined_2020, --extra-warmup-days 12, multi-trade, SHARD_COUNT=4)
2026-09-28 12:34:47 IST r16: sweep finished rc=0
2026-09-28 12:34:47 IST r16: reaper timer restarted
2026-09-28 12:34:47 IST r16: chain finished
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
== last 8 s6_status lines:
[2026-09-27T21:21:20Z] [r16] ==========================================
[2026-09-27T21:21:20Z] [r16] sweep [r16] -> data/historical/backtest_reports/s6_r16 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-27T21:21:20Z] [r16] ==========================================
[2026-09-27T21:21:20Z] [r16] --- full2020_base (renko_trend, src=combined_2020) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 8.33, "brick_source_timeframe_minutes": 5, "direction_fil
[2026-09-28T07:04:47Z] [r16] full2020_base OK (35007s, 4345 trades, 65G free)
[2026-09-28T07:04:47Z] [r16] ==========================================
[2026-09-28T07:04:47Z] [r16] sweep [r16] COMPLETE -> data/historical/backtest_reports/s6_r16 (583min)
[2026-09-28T07:04:47Z] [r16] ==========================================
== finished configs (all chains): 497
== md5:
53208abd backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
