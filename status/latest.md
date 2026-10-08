# btsync status  2026-10-08T23:55:17Z UTC / 2026-10-09 05:25:17 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 05:25:17 IST / 23:55:17 UTC  load: 4.35 4.52 4.59  free: 7G avail  disk: 55G free
== units:
  backtest-20261008-163306.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ser_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap11_chain.heartbeat
2026-10-09 04:12:20 IST fxvwap11: reaper timer stopped
2026-10-09 04:12:22 IST fxvwap11: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap10_chain.heartbeat
2026-10-09 01:13:54 IST fxvwap10: reaper timer stopped
2026-10-09 01:13:56 IST fxvwap10: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 04:12:20 IST fxvwap10: sweep finished rc=0
2026-10-09 04:12:20 IST fxvwap10: chain finished
-- fxvwap9_chain.heartbeat
2026-10-08 22:03:06 IST fxvwap9: reaper timer stopped
2026-10-08 22:03:07 IST fxvwap9: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 01:13:54 IST fxvwap9: sweep finished rc=0
2026-10-09 01:13:54 IST fxvwap9: chain finished
== last 8 s6_status lines:
[2026-10-08T22:42:20Z] [fxvwap10] VWAP_FX_rr12_t225a333 OK (10704s, 1215 trades, 55G free)
[2026-10-08T22:42:20Z] [fxvwap10] ==========================================
[2026-10-08T22:42:20Z] [fxvwap10] sweep [fxvwap10] COMPLETE -> data/historical/backtest_reports/s6_fxvwap10 (178min)
[2026-10-08T22:42:20Z] [fxvwap10] ==========================================
[2026-10-08T22:42:22Z] [fxvwap11] ==========================================
[2026-10-08T22:42:22Z] [fxvwap11] sweep [fxvwap11] -> data/historical/backtest_reports/s6_fxvwap11 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-08T22:42:22Z] [fxvwap11] ==========================================
[2026-10-08T22:42:22Z] [fxvwap11] --- VWAP_FX_rr11_s15t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.15, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "tra
== finished configs (all chains): 544
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
