# btsync status  2026-09-26T08:19:52Z UTC / 2026-09-26 13:49:52 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-26 13:49:52 IST / 08:19:52 UTC  load: 4.55 4.33 4.23  free: 7G avail  disk: 75G free
== units:
  backtest-20260926-060828.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && TAG=w12 END_BY_UTC=\"2026-09-28 02:00:00\" S
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- w12_chain.heartbeat
2026-09-26 11:38:28 IST w12: reaper timer stopped
2026-09-26 11:38:28 IST w12: frozen md5s: 587fefca 69ce1dd9 0bb606be cdec5753 dd220499 
2026-09-26 11:38:28 IST w12: chunk w12: launching sweep_configs/renko11_pilot.txt (1 configs, avg 4200s/cfg, SHARD_COUNT=4, extra='--extra-warmup-days 21')
-- mt1_chain.heartbeat
2026-09-26 01:10:21 IST mt1: reaper timer stopped
2026-09-26 01:10:21 IST mt1: launching renko10 multi-trade per-day (6 configs, SHARD_COUNT=4)
2026-09-26 06:27:30 IST mt1: batch finished rc=0 -- 6 OK (cumulative), 0 with failures
2026-09-26 06:27:30 IST mt1: reaper timer restarted
-- night2_chain.heartbeat
2026-09-26 00:25:51 IST night2: A: finished pd3_e4 rc=0
2026-09-26 00:25:53 IST night2: A: finished pd4_tf5x5 rc=0
2026-09-26 00:25:54 IST night2: A: finished pd5_b833mv50 rc=0
2026-09-26 00:25:54 IST night2: B: renko9 (standard harness)
2026-09-26 00:25:54 IST night2: chain finished -- perday1 OK: 2 ; renko9 OK: 0 (cumulative in status log)
2026-09-26 00:25:54 IST night2: reaper timer restarted
== last 8 s6_status lines:
[2026-09-26T00:57:30Z] [mt1] renko10_mt6_ctrl_cb1_nofilter OK (2985s, 1077 trades, 75G free)
[2026-09-26T00:57:30Z] [mt1] ==========================================
[2026-09-26T00:57:30Z] [mt1] sweep [mt1] COMPLETE -> data/historical/backtest_reports/s6_mt1 (317min)
[2026-09-26T00:57:30Z] [mt1] ==========================================
[2026-09-26T06:08:32Z] [w12] ==========================================
[2026-09-26T06:08:32Z] [w12] sweep [w12] -> data/historical/backtest_reports/s6_w12 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 21 --multi-trade'
[2026-09-26T06:08:32Z] [w12] ==========================================
[2026-09-26T06:08:32Z] [w12] --- renko11_p1_mv50_pe (renko_trend, src=alice_index) params={"brick_size_mode": "fixed", "fixed_brick_size_points": 6.25, "brick_source_timeframe_minutes": 15, "direction
== finished configs (all chains): 464
== md5:
587fefca backend/scripts/run_backtest.py
69ce1dd9 run_sweep_perday.sh
0bb606be run_sweep_default.sh
764ef01e launch_chain.sh
== ATTENTION:
ATTENTION: none
```
