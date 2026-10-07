# btsync status  2026-10-07T17:52:53Z UTC / 2026-10-07 23:22:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-07 23:22:53 IST / 17:52:53 UTC  load: 0.24 0.13 0.05  free: 8G avail  disk: 57G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxvwap1_chain.heartbeat
2026-10-07 15:35:17 IST fxvwap1: reaper timer stopped
2026-10-07 15:35:19 IST fxvwap1: QC ok; 1472 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-07 21:28:27 IST fxvwap1: sweep finished rc=0
2026-10-07 21:28:27 IST fxvwap1: chain finished
2026-10-07 21:28:27 IST fxvwap1: reaper timer restarted
-- fxema5_chain.heartbeat
2026-10-05 17:48:58 IST fxema5: reaper timer stopped
2026-10-05 17:49:00 IST fxema5: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 20:41:12 IST fxema5: sweep finished rc=0
2026-10-05 20:41:12 IST fxema5: chain finished
2026-10-05 20:41:12 IST fxema5: reaper timer restarted
-- fxema4_chain.heartbeat
2026-10-05 06:56:03 IST fxema4: reaper timer stopped
2026-10-05 06:56:05 IST fxema4: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-05 09:59:55 IST fxema4: sweep finished rc=0
2026-10-05 09:59:55 IST fxema4: chain finished
2026-10-05 09:59:55 IST fxema4: reaper timer restarted
== last 8 s6_status lines:
[2026-10-07T10:05:19Z] [fxvwap1] ==========================================
[2026-10-07T10:05:19Z] [fxvwap1] --- VWAP_FX_live (vwap_pullback_conviction, src=futures_proxy) params={"pcr_directional_ce_min": 1.1, "pcr_directional_pe_max": 1.0, "pcr_directional_ce_max2": 0.85, "
[2026-10-07T13:00:26Z] [fxvwap1] VWAP_FX_live OK (10507s, 13906 trades, 57G free)
[2026-10-07T13:00:26Z] [fxvwap1] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
[2026-10-07T15:58:27Z] [fxvwap1] VWAP_FX_nopcr OK (10681s, 20323 trades, 57G free)
[2026-10-07T15:58:27Z] [fxvwap1] ==========================================
[2026-10-07T15:58:27Z] [fxvwap1] sweep [fxvwap1] COMPLETE -> data/historical/backtest_reports/s6_fxvwap1 (353min)
[2026-10-07T15:58:27Z] [fxvwap1] ==========================================
== finished configs (all chains): 537
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
