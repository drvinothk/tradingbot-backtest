# btsync status  2026-10-07T20:51:57Z UTC / 2026-10-08 02:21:57 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-08 02:21:57 IST / 20:51:57 UTC  load: 5.03 4.76 4.73  free: 8G avail  disk: 56G free
== units:
  backtest-20261007-181522.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_fx_1007.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxorb1_chain.heartbeat
2026-10-07 23:45:22 IST fxorb1: reaper timer stopped
2026-10-07 23:45:23 IST fxorb1: QC ok; 1636 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
-- qcovl_on_chain.heartbeat
2026-10-07 23:41:59 IST qcovl_on: reaper timer stopped
2026-10-07 23:42:00 IST qcovl_on: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-07 23:43:56 IST qcovl_on: sweep finished rc=0
2026-10-07 23:43:56 IST qcovl_on: chain finished
-- qcovl_log_chain.heartbeat
2026-10-07 23:39:58 IST qcovl_log: reaper timer stopped
2026-10-07 23:39:59 IST qcovl_log: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 2d185d39
2026-10-07 23:41:59 IST qcovl_log: sweep finished rc=0
2026-10-07 23:41:59 IST qcovl_log: chain finished
== last 8 s6_status lines:
[2026-10-07T18:13:56Z] [qcovl_on] VWAP_FX_nopcr OK (116s, 63 trades, 57G free)
[2026-10-07T18:13:56Z] [qcovl_on] ==========================================
[2026-10-07T18:13:56Z] [qcovl_on] sweep [qcovl_on] COMPLETE -> data/historical/backtest_reports/s6_qcovl_on (1min)
[2026-10-07T18:13:56Z] [qcovl_on] ==========================================
[2026-10-07T18:15:23Z] [fxorb1] ==========================================
[2026-10-07T18:15:23Z] [fxorb1] sweep [fxorb1] -> data/historical/backtest_reports/s6_fxorb1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-07T18:15:23Z] [fxorb1] ==========================================
[2026-10-07T18:15:23Z] [fxorb1] --- ORB_FX_live (orb_conviction, src=combined_2020) params={"stop_pct": 0.2, "target_pct": 0.66, "trail_activation_fraction": 0.18, "trail_lock_fraction": 0.7, "orb_ent
== finished configs (all chains): 537
== md5:
2d185d39 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! newest config started/finished 9394s ago (>2.5h) while a unit is running -- possible stall
```
