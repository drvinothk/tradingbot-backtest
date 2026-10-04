# btsync status  2026-10-04T23:56:53Z UTC / 2026-10-05 05:26:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-05 05:26:53 IST / 23:56:53 UTC  load: 4.50 5.10 5.12  free: 8G avail  disk: 59G free
== units:
  backtest-20261004-184613.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_fxema3.sh"
  backtest-20261004-210148.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ALLOW_MARKET_WINDOW=1 ./chain_next.sh fxema3
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxema3_chain.heartbeat
2026-10-05 01:17:16 IST fxema3: reaper timer stopped
2026-10-05 01:17:18 IST fxema3: QC ok; 1636 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
-- fxema2_chain.heartbeat
2026-10-04 14:17:54 IST fxema2: reaper timer stopped
2026-10-04 14:17:56 IST fxema2: QC ok; 1636 day:expiry pairs, 4 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 01:16:11 IST fxema2: sweep finished rc=0
2026-10-05 01:16:11 IST fxema2: chain finished
2026-10-05 01:16:11 IST fxema2: reaper timer restarted
-- fxv1_chain.heartbeat
2026-10-04 13:09:58 IST fxv1: reaper timer stopped
2026-10-04 13:09:59 IST fxv1: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:11:05 IST fxv1: sweep finished rc=0
2026-10-04 13:11:05 IST fxv1: chain finished
== last 8 s6_status lines:
[2026-10-04T19:46:11Z] [fxema2] sweep [fxema2] COMPLETE -> data/historical/backtest_reports/s6_fxema2 (658min)
[2026-10-04T19:46:11Z] [fxema2] ==========================================
[2026-10-04T19:47:18Z] [fxema3] ==========================================
[2026-10-04T19:47:18Z] [fxema3] sweep [fxema3] -> data/historical/backtest_reports/s6_fxema3 (2 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-04T19:47:18Z] [fxema3] ==========================================
[2026-10-04T19:47:18Z] [fxema3] --- EMA_FX3_floor115_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
[2026-10-04T22:34:58Z] [fxema3] EMA_FX3_floor115_t05 OK (10060s, 1533 trades, 59G free)
[2026-10-04T22:34:58Z] [fxema3] --- EMA_FX3_floor120_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
== finished configs (all chains): 532
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
