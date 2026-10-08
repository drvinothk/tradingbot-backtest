# btsync status  2026-10-08T10:01:14Z UTC / 2026-10-08 15:31:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 15:31:14 IST / 10:01:14 UTC  load: 0.47 0.20 0.18  free: 7G avail  disk: 56G free
== units:
  backtest-20261008-074234.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rng_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- qcrng_off_chain.heartbeat
2026-10-08 15:31:05 IST qcrng_off: reaper timer stopped
2026-10-08 15:31:07 IST qcrng_off: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxema6_chain.heartbeat
2026-10-08 05:31:20 IST fxema6: reaper timer stopped
2026-10-08 05:31:22 IST fxema6: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 08:23:50 IST fxema6: sweep finished rc=0
2026-10-08 08:23:50 IST fxema6: chain finished
-- fxvwap2_chain.heartbeat
2026-10-08 02:31:03 IST fxvwap2: reaper timer stopped
2026-10-08 02:31:04 IST fxvwap2: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 05:31:20 IST fxvwap2: sweep finished rc=0
2026-10-08 05:31:20 IST fxvwap2: chain finished
== last 8 s6_status lines:
[2026-10-08T02:53:50Z] [fxema6] EMA_FX_r28_prem40 OK (10348s, 1422 trades, 57G free)
[2026-10-08T02:53:50Z] [fxema6] ==========================================
[2026-10-08T02:53:50Z] [fxema6] sweep [fxema6] COMPLETE -> data/historical/backtest_reports/s6_fxema6 (172min)
[2026-10-08T02:53:50Z] [fxema6] ==========================================
[2026-10-08T10:01:07Z] [qcrng_off] ==========================================
[2026-10-08T10:01:07Z] [qcrng_off] sweep [qcrng_off] -> data/historical/backtest_reports/s6_qcrng_off (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-08T10:01:07Z] [qcrng_off] ==========================================
[2026-10-08T10:01:07Z] [qcrng_off] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 540
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
