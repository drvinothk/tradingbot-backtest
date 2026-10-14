# btsync status  2026-10-14T09:18:20Z UTC / 2026-10-14 14:48:20 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-14 14:48:20 IST / 09:18:20 UTC  load: 2.82 4.00 2.80  free: 7G avail  disk: 51G free
== units:
  backtest-20261014-090511.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_volcmp_1014.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- vc_old_chain.heartbeat
2026-10-14 14:46:39 IST vc_old: reaper timer stopped
2026-10-14 14:46:40 IST vc_old: QC ok; 79 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- vc_new_chain.heartbeat
2026-10-14 14:35:11 IST vc_new: reaper timer stopped
2026-10-14 14:35:13 IST vc_new: QC ok; 79 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-14 14:46:38 IST vc_new: sweep finished rc=0
2026-10-14 14:46:38 IST vc_new: chain finished
2026-10-14 14:46:38 IST vc_new: reaper timer restarted
-- rem_col1p_chain.heartbeat
2026-10-13 12:23:39 IST rem_col1p: reaper timer stopped
2026-10-13 12:23:41 IST rem_col1p: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 14:15:36 IST rem_col1p: sweep finished rc=0
2026-10-13 14:15:36 IST rem_col1p: chain finished
2026-10-13 14:15:36 IST rem_col1p: reaper timer restarted
== last 8 s6_status lines:
[2026-10-14T09:16:38Z] [vc_new] ==========================================
[2026-10-14T09:16:38Z] [vc_new] sweep [vc_new] COMPLETE -> data/historical/backtest_reports/s6_vc_new (11min)
[2026-10-14T09:16:38Z] [vc_new] ==========================================
[2026-10-14T09:16:40Z] [vc_old] ==========================================
[2026-10-14T09:16:40Z] [vc_old] sweep [vc_old] -> data/historical/backtest_reports/s6_vc_old (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-14T09:16:40Z] [vc_old] data_through=2026-10-13 pairs=/home/ubuntu/backtest_engine/sweep_configs/pairs_volcmp_20261014.txt
[2026-10-14T09:16:40Z] [vc_old] ==========================================
[2026-10-14T09:16:40Z] [vc_old] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
81d4fcc0 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
