# btsync status  2026-10-13T08:28:23Z UTC / 2026-10-13 13:58:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 13:58:24 IST / 08:28:24 UTC  load: 4.49 4.25 4.30  free: 6G avail  disk: 51G free
== units:
  backtest-20261013-065339.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./run_rem_col1p.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rem_col1p_chain.heartbeat
2026-10-13 12:23:39 IST rem_col1p: reaper timer stopped
2026-10-13 12:23:41 IST rem_col1p: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- col_tri_chain.heartbeat
2026-10-13 03:39:26 IST col_tri: reaper timer stopped
2026-10-13 03:39:27 IST col_tri: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 04:46:02 IST col_tri: sweep finished rc=0
2026-10-13 04:46:02 IST col_tri: chain finished
-- col_all3_chain.heartbeat
2026-10-13 02:31:32 IST col_all3: reaper timer stopped
2026-10-13 02:31:34 IST col_all3: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 03:39:26 IST col_all3: sweep finished rc=0
2026-10-13 03:39:26 IST col_all3: chain finished
== last 8 s6_status lines:
[2026-10-12T23:16:02Z] [col_tri] VWAP_FX_s15_expatm_p250 OK (3995s, 171 trades, 51G free)
[2026-10-12T23:16:02Z] [col_tri] ==========================================
[2026-10-12T23:16:02Z] [col_tri] sweep [col_tri] COMPLETE -> data/historical/backtest_reports/s6_col_tri (66min)
[2026-10-12T23:16:02Z] [col_tri] ==========================================
[2026-10-13T06:53:41Z] [rem_col1p] ==========================================
[2026-10-13T06:53:41Z] [rem_col1p] sweep [rem_col1p] -> data/historical/backtest_reports/s6_rem_col1p (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-13T06:53:41Z] [rem_col1p] ==========================================
[2026-10-13T06:53:41Z] [rem_col1p] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activat
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
