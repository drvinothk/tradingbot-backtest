# btsync status  2026-10-09T20:41:42Z UTC / 2026-10-10 02:11:42 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-10 02:11:43 IST / 20:41:43 UTC  load: 4.67 4.73 4.72  free: 7G avail  disk: 54G free
== units:
  backtest-20261009-165623.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_htf15_1009.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- fxvwap16_chain.heartbeat
2026-10-10 01:09:25 IST fxvwap16: reaper timer stopped
2026-10-10 01:09:27 IST fxvwap16: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
-- fxvwap15_chain.heartbeat
2026-10-09 22:36:54 IST fxvwap15: reaper timer stopped
2026-10-09 22:36:55 IST fxvwap15: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-10 01:09:25 IST fxvwap15: sweep finished rc=0
2026-10-10 01:09:25 IST fxvwap15: chain finished
-- qch15_norr_chain.heartbeat
2026-10-09 22:35:11 IST qch15_norr: reaper timer stopped
2026-10-09 22:35:13 IST qch15_norr: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 937113b0
2026-10-09 22:36:53 IST qch15_norr: sweep finished rc=0
2026-10-09 22:36:53 IST qch15_norr: chain finished
== last 8 s6_status lines:
[2026-10-09T19:39:25Z] [fxvwap15] VWAP_FX_h15_c1245 OK (9150s, 436 trades, 54G free)
[2026-10-09T19:39:25Z] [fxvwap15] ==========================================
[2026-10-09T19:39:25Z] [fxvwap15] sweep [fxvwap15] COMPLETE -> data/historical/backtest_reports/s6_fxvwap15 (152min)
[2026-10-09T19:39:25Z] [fxvwap15] ==========================================
[2026-10-09T19:39:27Z] [fxvwap16] ==========================================
[2026-10-09T19:39:27Z] [fxvwap16] sweep [fxvwap16] -> data/historical/backtest_reports/s6_fxvwap16 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-09T19:39:27Z] [fxvwap16] ==========================================
[2026-10-09T19:39:27Z] [fxvwap16] --- VWAP_FX_h15_s30t50 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.002, "max_vwap_crosses_in_lookback": 1, "trail_activation_fr
== finished configs (all chains): 554
== md5:
937113b0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
