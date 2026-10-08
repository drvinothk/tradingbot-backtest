# btsync status  2026-10-08T16:36:20Z UTC / 2026-10-08 22:06:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 22:06:20 IST / 16:36:20 UTC  load: 5.34 4.85 4.25  free: 7G avail  disk: 55G free
== units:
  backtest-20261008-163306.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ser_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap9_chain.heartbeat
2026-10-08 22:03:06 IST fxvwap9: reaper timer stopped
2026-10-08 22:03:07 IST fxvwap9: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap5_chain.heartbeat
2026-10-08 21:48:48 IST fxvwap5: reaper timer stopped
2026-10-08 21:48:49 IST fxvwap5: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap4_chain.heartbeat
2026-10-08 18:40:24 IST fxvwap4: reaper timer stopped
2026-10-08 18:40:26 IST fxvwap4: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-08 21:41:23 IST fxvwap4: sweep finished rc=0
2026-10-08 21:41:23 IST fxvwap4: chain finished
== last 8 s6_status lines:
[2026-10-08T16:18:49Z] [fxvwap5] ==========================================
[2026-10-08T16:18:49Z] [fxvwap5] sweep [fxvwap5] -> data/historical/backtest_reports/s6_fxvwap5 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-08T16:18:49Z] [fxvwap5] ==========================================
[2026-10-08T16:18:49Z] [fxvwap5] --- VWAP_FX_rr12_t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.1, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "trail_lo
[2026-10-08T16:33:07Z] [fxvwap9] ==========================================
[2026-10-08T16:33:07Z] [fxvwap9] sweep [fxvwap9] -> data/historical/backtest_reports/s6_fxvwap9 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-08T16:33:07Z] [fxvwap9] ==========================================
[2026-10-08T16:33:07Z] [fxvwap9] --- VWAP_FX_rr11_t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.1, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "trail_lo
== finished configs (all chains): 542
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
