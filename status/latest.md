# btsync status  2026-10-09T06:02:50Z UTC / 2026-10-09 11:32:50 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-09 11:32:50 IST / 06:02:50 UTC  load: 0.18 0.33 0.63  free: 8G avail  disk: 55G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxvwap12_chain.heartbeat
2026-10-09 07:12:27 IST fxvwap12: reaper timer stopped
2026-10-09 07:12:29 IST fxvwap12: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine a30b943b
2026-10-09 10:52:58 IST fxvwap12: sweep finished rc=0
2026-10-09 10:52:58 IST fxvwap12: chain finished
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
[2026-10-09T01:42:29Z] [fxvwap12] ==========================================
[2026-10-09T01:42:29Z] [fxvwap12] sweep [fxvwap12] -> data/historical/backtest_reports/s6_fxvwap12 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T01:42:29Z] [fxvwap12] ==========================================
[2026-10-09T01:42:29Z] [fxvwap12] --- VWAP_FX_rr12_s15t225a333 (vwap_pullback_conviction, src=futures_proxy) params={"stop_pct": 0.15, "target_pct": 0.225, "trail_activation_fraction": 0.3333333, "tra
[2026-10-09T05:22:58Z] [fxvwap12] VWAP_FX_rr12_s15t225a333 OK (13229s, 1159 trades, 55G free)
[2026-10-09T05:22:58Z] [fxvwap12] ==========================================
[2026-10-09T05:22:58Z] [fxvwap12] sweep [fxvwap12] COMPLETE -> data/historical/backtest_reports/s6_fxvwap12 (220min)
[2026-10-09T05:22:58Z] [fxvwap12] ==========================================
== finished configs (all chains): 546
== md5:
a30b943b backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
