# btsync status  2026-10-07T15:04:20Z UTC / 2026-10-07 20:34:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-07 20:34:21 IST / 15:04:21 UTC  load: 4.51 4.57 4.60  free: 6G avail  disk: 57G free
== units:
  backtest-20261007-100517.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./launch_config_run_optvol.sh fxvwap1 sweep_
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxvwap1_chain.heartbeat
2026-10-07 15:35:17 IST fxvwap1: reaper timer stopped
2026-10-07 15:35:19 IST fxvwap1: QC ok; 1472 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
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
[2026-10-05T15:11:12Z] [fxema5] sweep [fxema5] COMPLETE -> data/historical/backtest_reports/s6_fxema5 (172min)
[2026-10-05T15:11:12Z] [fxema5] ==========================================
[2026-10-07T10:05:19Z] [fxvwap1] ==========================================
[2026-10-07T10:05:19Z] [fxvwap1] sweep [fxvwap1] -> data/historical/backtest_reports/s6_fxvwap1 (2 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-07T10:05:19Z] [fxvwap1] ==========================================
[2026-10-07T10:05:19Z] [fxvwap1] --- VWAP_FX_live (vwap_pullback_conviction, src=futures_proxy) params={"pcr_directional_ce_min": 1.1, "pcr_directional_pe_max": 1.0, "pcr_directional_ce_max2": 0.85, "
[2026-10-07T13:00:26Z] [fxvwap1] VWAP_FX_live OK (10507s, 13906 trades, 57G free)
[2026-10-07T13:00:26Z] [fxvwap1] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 536
== md5:
b3b361d7 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
