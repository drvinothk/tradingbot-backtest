# btsync status  2026-10-08T10:03:34Z UTC / 2026-10-08 15:33:34 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 15:33:34 IST / 10:03:34 UTC  load: 3.80 1.82 0.80  free: 7G avail  disk: 56G free
== units:
  backtest-20261008-074234.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rng_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- qcrng_log_chain.heartbeat
2026-10-08 15:33:22 IST qcrng_log: reaper timer stopped
2026-10-08 15:33:24 IST qcrng_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- qcrng_off_chain.heartbeat
2026-10-08 15:31:05 IST qcrng_off: reaper timer stopped
2026-10-08 15:31:07 IST qcrng_off: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 15:33:22 IST qcrng_off: sweep finished rc=0
2026-10-08 15:33:22 IST qcrng_off: chain finished
-- fxema6_chain.heartbeat
2026-10-08 05:31:20 IST fxema6: reaper timer stopped
2026-10-08 05:31:22 IST fxema6: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 08:23:50 IST fxema6: sweep finished rc=0
2026-10-08 08:23:50 IST fxema6: chain finished
== last 8 s6_status lines:
[2026-10-08T10:03:22Z] [qcrng_off] VWAP_FX_nopcr OK (135s, 224 trades, 56G free)
[2026-10-08T10:03:22Z] [qcrng_off] ==========================================
[2026-10-08T10:03:22Z] [qcrng_off] sweep [qcrng_off] COMPLETE -> data/historical/backtest_reports/s6_qcrng_off (2min)
[2026-10-08T10:03:22Z] [qcrng_off] ==========================================
[2026-10-08T10:03:24Z] [qcrng_log] ==========================================
[2026-10-08T10:03:24Z] [qcrng_log] sweep [qcrng_log] -> data/historical/backtest_reports/s6_qcrng_log (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-08T10:03:24Z] [qcrng_log] ==========================================
[2026-10-08T10:03:24Z] [qcrng_log] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 540
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: fflush failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
