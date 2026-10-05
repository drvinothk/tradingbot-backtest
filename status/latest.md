# btsync status  2026-10-05T04:26:51Z UTC / 2026-10-05 09:56:51 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-05 09:56:51 IST / 04:26:51 UTC  load: 3.04 4.05 4.44  free: 6G avail  disk: 59G free
== units:
  backtest-20261004-210148.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ALLOW_MARKET_WINDOW=1 ./chain_next.sh fxema3
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxema4_chain.heartbeat
2026-10-05 06:56:03 IST fxema4: reaper timer stopped
2026-10-05 06:56:05 IST fxema4: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
-- fxema3_chain.heartbeat
2026-10-05 01:17:16 IST fxema3: reaper timer stopped
2026-10-05 01:17:18 IST fxema3: QC ok; 1636 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 06:54:33 IST fxema3: sweep finished rc=0
2026-10-05 06:54:33 IST fxema3: chain finished
2026-10-05 06:54:33 IST fxema3: reaper timer restarted
-- fxema2_chain.heartbeat
2026-10-04 14:17:54 IST fxema2: reaper timer stopped
2026-10-04 14:17:56 IST fxema2: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 01:16:11 IST fxema2: sweep finished rc=0
2026-10-05 01:16:11 IST fxema2: chain finished
2026-10-05 01:16:11 IST fxema2: reaper timer restarted
== last 8 s6_status lines:
[2026-10-05T01:24:33Z] [fxema3] EMA_FX3_floor120_t05 OK (10175s, 1326 trades, 59G free)
[2026-10-05T01:24:33Z] [fxema3] ==========================================
[2026-10-05T01:24:33Z] [fxema3] sweep [fxema3] COMPLETE -> data/historical/backtest_reports/s6_fxema3 (337min)
[2026-10-05T01:24:33Z] [fxema3] ==========================================
[2026-10-05T01:26:05Z] [fxema4] ==========================================
[2026-10-05T01:26:05Z] [fxema4] sweep [fxema4] -> data/historical/backtest_reports/s6_fxema4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-05T01:26:05Z] [fxema4] ==========================================
[2026-10-05T01:26:05Z] [fxema4] --- EMA_FX4_floor130_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
== finished configs (all chains): 533
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 10846s ago (>2.5h) while a unit is running -- possible stall
```
