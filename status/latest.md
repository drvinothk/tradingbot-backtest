# btsync status  2026-10-08T15:41:45Z UTC / 2026-10-08 21:11:45 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 21:11:45 IST / 15:41:45 UTC  load: 4.90 4.72 4.66  free: 6G avail  disk: 55G free
== units:
  backtest-20261008-074234.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rng_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap4_chain.heartbeat
2026-10-08 18:40:24 IST fxvwap4: reaper timer stopped
2026-10-08 18:40:26 IST fxvwap4: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap3_chain.heartbeat
2026-10-08 15:38:15 IST fxvwap3: reaper timer stopped
2026-10-08 15:38:16 IST fxvwap3: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 18:40:24 IST fxvwap3: sweep finished rc=0
2026-10-08 18:40:24 IST fxvwap3: chain finished
-- qcrng_on_chain.heartbeat
2026-10-08 15:35:52 IST qcrng_on: reaper timer stopped
2026-10-08 15:35:54 IST qcrng_on: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 15:38:11 IST qcrng_on: sweep finished rc=0
2026-10-08 15:38:11 IST qcrng_on: chain finished
== last 8 s6_status lines:
[2026-10-08T13:10:24Z] [fxvwap3] VWAP_FX_stack_rr11 OK (10928s, 1625 trades, 56G free)
[2026-10-08T13:10:24Z] [fxvwap3] ==========================================
[2026-10-08T13:10:24Z] [fxvwap3] sweep [fxvwap3] COMPLETE -> data/historical/backtest_reports/s6_fxvwap3 (182min)
[2026-10-08T13:10:24Z] [fxvwap3] ==========================================
[2026-10-08T13:10:26Z] [fxvwap4] ==========================================
[2026-10-08T13:10:26Z] [fxvwap4] sweep [fxvwap4] -> data/historical/backtest_reports/s6_fxvwap4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-08T13:10:26Z] [fxvwap4] ==========================================
[2026-10-08T13:10:26Z] [fxvwap4] --- VWAP_FX_stack_rr12 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 541
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9079s ago (>2.5h) while a unit is running -- possible stall
```
