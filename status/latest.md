# btsync status  2026-10-07T21:13:22Z UTC / 2026-10-08 02:43:22 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 02:43:22 IST / 21:13:22 UTC  load: 4.91 4.72 4.72  free: 9G avail  disk: 56G free
== units:
  backtest-20261007-181522.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_fx_1007.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: fflush failed: 'standard output': Broken pipe
sort: write error
-- fxvwap2_chain.heartbeat
2026-10-08 02:31:03 IST fxvwap2: reaper timer stopped
2026-10-08 02:31:04 IST fxvwap2: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
-- fxorb1_chain.heartbeat
2026-10-07 23:45:22 IST fxorb1: reaper timer stopped
2026-10-07 23:45:23 IST fxorb1: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-08 02:31:03 IST fxorb1: sweep finished rc=0
2026-10-08 02:31:03 IST fxorb1: chain finished
-- qcovl_on_chain.heartbeat
2026-10-07 23:41:59 IST qcovl_on: reaper timer stopped
2026-10-07 23:42:00 IST qcovl_on: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-07 23:43:56 IST qcovl_on: sweep finished rc=0
2026-10-07 23:43:56 IST qcovl_on: chain finished
== last 8 s6_status lines:
[2026-10-07T21:01:02Z] [fxorb1] ORB_FX_live OK (9939s, 897 trades, 57G free)
[2026-10-07T21:01:02Z] [fxorb1] ==========================================
[2026-10-07T21:01:02Z] [fxorb1] sweep [fxorb1] COMPLETE -> data/historical/backtest_reports/s6_fxorb1 (165min)
[2026-10-07T21:01:02Z] [fxorb1] ==========================================
[2026-10-07T21:01:04Z] [fxvwap2] ==========================================
[2026-10-07T21:01:04Z] [fxvwap2] sweep [fxvwap2] -> data/historical/backtest_reports/s6_fxvwap2 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-07T21:01:04Z] [fxvwap2] ==========================================
[2026-10-07T21:01:04Z] [fxvwap2] --- VWAP_FX_nopcr_stack (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 538
== md5:
2d185d39 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
