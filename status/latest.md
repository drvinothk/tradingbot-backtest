# btsync status  2026-09-26T13:10:33Z UTC / 2026-09-26 18:40:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-26 18:40:33 IST / 13:10:33 UTC  load: 4.48 4.52 4.49  free: 7G avail  disk: 75G free
== units:
  backtest-20260926-082551.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && TAG=w13 END_BY_UTC=\"2026-09-28 02:00:00\" S
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- w13_chain.heartbeat
2026-09-26 13:55:51 IST w13: reaper timer stopped
2026-09-26 13:55:51 IST w13: frozen md5s: 6a26192c 587fefca 69ce1dd9 0bb606be cdec5753 dd220499 
2026-09-26 13:55:51 IST w13: chunk w13a: launching sweep_configs/renko12a_warm_batch.txt (4 configs, avg 4200s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
2026-09-26 17:37:54 IST w13: chunk w13a: rc=0 13323s ok=4 shard-failures=0 tracebacks=0
2026-09-26 17:37:54 IST w13: chunk w13b: launching sweep_configs/renko12b_warm_batch.txt (4 configs, avg 3330s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 12')
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
[2026-09-26T12:07:54Z] [w13a] sweep [w13a] COMPLETE -> data/historical/backtest_reports/s6_w13a (222min)
[2026-09-26T12:07:54Z] [w13a] ==========================================
[2026-09-26T12:07:57Z] [w13b] ==========================================
[2026-09-26T12:07:57Z] [w13b] sweep [w13b] -> data/historical/backtest_reports/s6_w13b (4 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-26T12:07:57Z] [w13b] ==========================================
[2026-09-26T12:07:57Z] [w13b] --- w12_s1_m075 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 0.75, "confirm_bricks": 2, "entry_mode": "br
[2026-09-26T12:57:59Z] [w13b] w12_s1_m075 OK (3002s, 237 trades, 75G free)
[2026-09-26T12:57:59Z] [w13b] --- w12_s1_m05 (renko_trend, src=alice_index) params={"htf_timeframe_minutes": 30, "atr_period": 14, "brick_atr_multiplier": 0.5, "confirm_bricks": 2, "entry_mode": "brea
== finished configs (all chains): 470
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
