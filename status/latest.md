# btsync status  2026-10-07T18:14:56Z UTC / 2026-10-07 23:44:56 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-07 23:44:56 IST / 18:14:56 UTC  load: 1.54 2.45 1.30  free: 8G avail  disk: 57G free
== units:
(none running)
== run_backtest procs: 1   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- fxema6_chain.heartbeat
2026-10-07 23:44:56 IST fxema6: ABORT -- a sweep is running
-- fxvwap2_chain.heartbeat
2026-10-07 23:44:55 IST fxvwap2: ABORT -- a sweep is running
-- fxorb1_chain.heartbeat
2026-10-07 23:44:55 IST fxorb1: ABORT -- a sweep is running
== last 8 s6_status lines:
[2026-10-07T18:12:00Z] [qcovl_on] ==========================================
[2026-10-07T18:12:00Z] [qcovl_on] sweep [qcovl_on] -> data/historical/backtest_reports/s6_qcovl_on (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-07T18:12:00Z] [qcovl_on] ==========================================
[2026-10-07T18:12:00Z] [qcovl_on] --- VWAP_FX_nopcr (vwap_pullback_conviction, src=futures_proxy) params={}
[2026-10-07T18:13:56Z] [qcovl_on] VWAP_FX_nopcr OK (116s, 63 trades, 57G free)
[2026-10-07T18:13:56Z] [qcovl_on] ==========================================
[2026-10-07T18:13:56Z] [qcovl_on] sweep [qcovl_on] COMPLETE -> data/historical/backtest_reports/s6_qcovl_on (1min)
[2026-10-07T18:13:56Z] [qcovl_on] ==========================================
== finished configs (all chains): 537
== md5:
2d185d39 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! chain fxema6_chain.heartbeat ended without a finish line (last: 2026-10-07 23:44:56 IST fxema6: ABORT -- a sweep is running)
! fxema6_chain.heartbeat: 2026-10-07 23:44:56 IST fxema6: ABORT -- a sweep is running
! chain fxvwap2_chain.heartbeat ended without a finish line (last: 2026-10-07 23:44:55 IST fxvwap2: ABORT -- a sweep is running)
! fxvwap2_chain.heartbeat: 2026-10-07 23:44:55 IST fxvwap2: ABORT -- a sweep is running
! chain fxorb1_chain.heartbeat ended without a finish line (last: 2026-10-07 23:44:55 IST fxorb1: ABORT -- a sweep is running)
! fxorb1_chain.heartbeat: 2026-10-07 23:44:55 IST fxorb1: ABORT -- a sweep is running
```
