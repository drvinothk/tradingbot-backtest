# btsync status  2026-10-08T19:46:10Z UTC / 2026-10-09 01:16:10 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 01:16:10 IST / 19:46:10 UTC  load: 4.51 4.42 4.53  free: 8G avail  disk: 55G free
== units:
  backtest-20261008-163306.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ser_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap10_chain.heartbeat
2026-10-09 01:13:54 IST fxvwap10: reaper timer stopped
2026-10-09 01:13:56 IST fxvwap10: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap9_chain.heartbeat
2026-10-08 22:03:06 IST fxvwap9: reaper timer stopped
2026-10-08 22:03:07 IST fxvwap9: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 01:13:54 IST fxvwap9: sweep finished rc=0
2026-10-09 01:13:54 IST fxvwap9: chain finished
-- fxvwap5_chain.heartbeat
2026-10-08 21:48:48 IST fxvwap5: reaper timer stopped
2026-10-08 21:48:49 IST fxvwap5: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
== last 8 s6_status lines:
[2026-10-08T19:43:54Z] [fxvwap9] VWAP_FX_rr11_t225a333 OK (11447s, 1623 trades, 55G free)
[2026-10-08T19:43:54Z] [fxvwap9] ==========================================
[2026-10-08T19:43:54Z] [fxvwap9] sweep [fxvwap9] COMPLETE -> data/historical/backtest_reports/s6_fxvwap9 (190min)
[2026-10-08T19:43:54Z] [fxvwap9] ==========================================
[2026-10-08T19:43:56Z] [fxvwap10] ==========================================
[2026-10-08T19:43:56Z] [fxvwap10] sweep [fxvwap10] -> data/historical/backtest_reports/s6_fxvwap10 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-08T19:43:56Z] [fxvwap10] ==========================================
[2026-10-08T19:43:56Z] [fxvwap10] --- VWAP_FX_rr12_t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.1, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "trail_l
== finished configs (all chains): 543
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
