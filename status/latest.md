# btsync status  2026-10-05T01:25:23Z UTC / 2026-10-05 06:55:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-05 06:55:23 IST / 01:25:23 UTC  load: 1.32 3.63 4.35  free: 10G avail  disk: 59G free
== units:
  backtest-20261004-210148.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ALLOW_MARKET_WINDOW=1 ./chain_next.sh fxema3
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
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
-- fxv1_chain.heartbeat
2026-10-04 13:09:58 IST fxv1: reaper timer stopped
2026-10-04 13:09:59 IST fxv1: QC ok; 8 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-04 13:11:05 IST fxv1: sweep finished rc=0
2026-10-04 13:11:05 IST fxv1: chain finished
== last 8 s6_status lines:
[2026-10-04T19:47:18Z] [fxema3] ==========================================
[2026-10-04T19:47:18Z] [fxema3] --- EMA_FX3_floor115_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
[2026-10-04T22:34:58Z] [fxema3] EMA_FX3_floor115_t05 OK (10060s, 1533 trades, 59G free)
[2026-10-04T22:34:58Z] [fxema3] --- EMA_FX3_floor120_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_
[2026-10-05T01:24:33Z] [fxema3] EMA_FX3_floor120_t05 OK (10175s, 1326 trades, 59G free)
[2026-10-05T01:24:33Z] [fxema3] ==========================================
[2026-10-05T01:24:33Z] [fxema3] sweep [fxema3] COMPLETE -> data/historical/backtest_reports/s6_fxema3 (337min)
[2026-10-05T01:24:33Z] [fxema3] ==========================================
== finished configs (all chains): 533
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
