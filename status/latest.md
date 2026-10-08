# btsync status  2026-10-08T12:13:54Z UTC / 2026-10-08 17:43:54 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 17:43:54 IST / 12:13:54 UTC  load: 4.49 4.60 4.62  free: 5G avail  disk: 55G free
== units:
  backtest-20261008-074234.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rng_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap3_chain.heartbeat
2026-10-08 15:38:15 IST fxvwap3: reaper timer stopped
2026-10-08 15:38:16 IST fxvwap3: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- qcrng_on_chain.heartbeat
2026-10-08 15:35:52 IST qcrng_on: reaper timer stopped
2026-10-08 15:35:54 IST qcrng_on: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 15:38:11 IST qcrng_on: sweep finished rc=0
2026-10-08 15:38:11 IST qcrng_on: chain finished
-- qcrng_log_chain.heartbeat
2026-10-08 15:33:22 IST qcrng_log: reaper timer stopped
2026-10-08 15:33:24 IST qcrng_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 15:35:52 IST qcrng_log: sweep finished rc=0
2026-10-08 15:35:52 IST qcrng_log: chain finished
== last 8 s6_status lines:
[2026-10-08T10:08:11Z] [qcrng_on] VWAP_FX_stack_rr11 OK (137s, 16 trades, 56G free)
[2026-10-08T10:08:11Z] [qcrng_on] ==========================================
[2026-10-08T10:08:11Z] [qcrng_on] sweep [qcrng_on] COMPLETE -> data/historical/backtest_reports/s6_qcrng_on (2min)
[2026-10-08T10:08:11Z] [qcrng_on] ==========================================
[2026-10-08T10:08:16Z] [fxvwap3] ==========================================
[2026-10-08T10:08:16Z] [fxvwap3] sweep [fxvwap3] -> data/historical/backtest_reports/s6_fxvwap3 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-08T10:08:16Z] [fxvwap3] ==========================================
[2026-10-08T10:08:16Z] [fxvwap3] --- VWAP_FX_stack_rr11 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 541
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
