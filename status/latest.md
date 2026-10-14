# btsync status  2026-10-14T09:06:04Z UTC / 2026-10-14 14:36:04 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-14 14:36:04 IST / 09:06:04 UTC  load: 2.86 1.04 0.58  free: 7G avail  disk: 51G free
== units:
  backtest-20261014-090511.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_volcmp_1014.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- vc_new_chain.heartbeat
2026-10-14 14:35:11 IST vc_new: reaper timer stopped
2026-10-14 14:35:13 IST vc_new: QC ok; 79 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- rem_col1p_chain.heartbeat
2026-10-13 12:23:39 IST rem_col1p: reaper timer stopped
2026-10-13 12:23:41 IST rem_col1p: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 14:15:36 IST rem_col1p: sweep finished rc=0
2026-10-13 14:15:36 IST rem_col1p: chain finished
2026-10-13 14:15:36 IST rem_col1p: reaper timer restarted
-- col_tri_chain.heartbeat
2026-10-13 03:39:26 IST col_tri: reaper timer stopped
2026-10-13 03:39:27 IST col_tri: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 04:46:02 IST col_tri: sweep finished rc=0
2026-10-13 04:46:02 IST col_tri: chain finished
== last 8 s6_status lines:
[2026-10-13T08:45:36Z] [rem_col1p] ==========================================
[2026-10-13T08:45:36Z] [rem_col1p] sweep [rem_col1p] COMPLETE -> data/historical/backtest_reports/s6_rem_col1p (111min)
[2026-10-13T08:45:36Z] [rem_col1p] ==========================================
[2026-10-14T09:05:13Z] [vc_new] ==========================================
[2026-10-14T09:05:13Z] [vc_new] sweep [vc_new] -> data/historical/backtest_reports/s6_vc_new (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-14T09:05:13Z] [vc_new] data_through=2026-10-13 pairs=/home/ubuntu/backtest_engine/sweep_configs/pairs_volcmp_20261014.txt
[2026-10-14T09:05:13Z] [vc_new] ==========================================
[2026-10-14T09:05:13Z] [vc_new] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
81d4fcc0 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
