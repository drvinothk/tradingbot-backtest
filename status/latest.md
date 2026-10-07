# btsync status  2026-10-07T18:10:30Z UTC / 2026-10-07 23:40:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-07 23:40:30 IST / 18:10:30 UTC  load: 3.91 1.71 0.65  free: 7G avail  disk: 57G free
== units:
  backtest-20261007-180802.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./qc_ovl_1007.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- qcovl_log_chain.heartbeat
2026-10-07 23:39:58 IST qcovl_log: reaper timer stopped
2026-10-07 23:39:59 IST qcovl_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
-- qcovl_off_chain.heartbeat
2026-10-07 23:38:02 IST qcovl_off: reaper timer stopped
2026-10-07 23:38:04 IST qcovl_off: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-07 23:39:58 IST qcovl_off: sweep finished rc=0
2026-10-07 23:39:58 IST qcovl_off: chain finished
-- fxvwap1_chain.heartbeat
2026-10-07 15:35:17 IST fxvwap1: reaper timer stopped
2026-10-07 15:35:19 IST fxvwap1: QC ok; 1472 day:expiry pairs, 2 config(s), SHARD_COUNT=4, engine b3b361d7
2026-10-07 21:28:27 IST fxvwap1: sweep finished rc=0
2026-10-07 21:28:27 IST fxvwap1: chain finished
2026-10-07 21:28:27 IST fxvwap1: reaper timer restarted
== last 8 s6_status lines:
[2026-10-07T18:09:57Z] [qcovl_off] VWAP_FX_nopcr OK (113s, 224 trades, 57G free)
[2026-10-07T18:09:57Z] [qcovl_off] ==========================================
[2026-10-07T18:09:57Z] [qcovl_off] sweep [qcovl_off] COMPLETE -> data/historical/backtest_reports/s6_qcovl_off (1min)
[2026-10-07T18:09:57Z] [qcovl_off] ==========================================
[2026-10-07T18:09:59Z] [qcovl_log] ==========================================
[2026-10-07T18:09:59Z] [qcovl_log] sweep [qcovl_log] -> data/historical/backtest_reports/s6_qcovl_log (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-07T18:09:59Z] [qcovl_log] ==========================================
[2026-10-07T18:09:59Z] [qcovl_log] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 537
== md5:
2d185d39 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
