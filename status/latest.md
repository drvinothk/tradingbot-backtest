# btsync status  2026-10-09T04:22:23Z UTC / 2026-10-09 09:52:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 09:52:23 IST / 04:22:23 UTC  load: 5.09 4.68 4.40  free: 6G avail  disk: 55G free
== units:
  backtest-20261008-163306.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_ser_1008.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap12_chain.heartbeat
2026-10-09 07:12:27 IST fxvwap12: reaper timer stopped
2026-10-09 07:12:29 IST fxvwap12: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
-- fxvwap11_chain.heartbeat
2026-10-09 04:12:20 IST fxvwap11: reaper timer stopped
2026-10-09 04:12:22 IST fxvwap11: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 07:12:26 IST fxvwap11: sweep finished rc=0
2026-10-09 07:12:26 IST fxvwap11: chain finished
-- fxvwap10_chain.heartbeat
2026-10-09 01:13:54 IST fxvwap10: reaper timer stopped
2026-10-09 01:13:56 IST fxvwap10: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 04:12:20 IST fxvwap10: sweep finished rc=0
2026-10-09 04:12:20 IST fxvwap10: chain finished
== last 8 s6_status lines:
[2026-10-09T01:42:26Z] [fxvwap11] VWAP_FX_rr11_s15t225a333 OK (10804s, 1546 trades, 55G free)
[2026-10-09T01:42:26Z] [fxvwap11] ==========================================
[2026-10-09T01:42:26Z] [fxvwap11] sweep [fxvwap11] COMPLETE -> data/historical/backtest_reports/s6_fxvwap11 (180min)
[2026-10-09T01:42:26Z] [fxvwap11] ==========================================
[2026-10-09T01:42:29Z] [fxvwap12] ==========================================
[2026-10-09T01:42:29Z] [fxvwap12] sweep [fxvwap12] -> data/historical/backtest_reports/s6_fxvwap12 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T01:42:29Z] [fxvwap12] ==========================================
[2026-10-09T01:42:29Z] [fxvwap12] --- VWAP_FX_rr12_s15t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.15, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "tra
== finished configs (all chains): 545
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9595s ago (>2.5h) while a unit is running -- possible stall
```
