# btsync status  2026-10-12T21:37:51Z UTC / 2026-10-13 03:07:51 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 03:07:51 IST / 21:37:51 UTC  load: 4.86 4.73 4.74  free: 8G avail  disk: 51G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- col_all3_chain.heartbeat
2026-10-13 02:31:32 IST col_all3: reaper timer stopped
2026-10-13 02:31:34 IST col_all3: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- col_1p_chain.heartbeat
2026-10-13 01:22:49 IST col_1p: reaper timer stopped
2026-10-13 01:22:50 IST col_1p: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 02:31:32 IST col_1p: sweep finished rc=0
2026-10-13 02:31:32 IST col_1p: chain finished
-- rem_vwap1_chain.heartbeat
2026-10-12 23:53:52 IST rem_vwap1: reaper timer stopped
2026-10-12 23:53:54 IST rem_vwap1: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 01:22:49 IST rem_vwap1: sweep finished rc=0
2026-10-13 01:22:49 IST rem_vwap1: chain finished
== last 8 s6_status lines:
[2026-10-12T21:01:32Z] [col_1p] VWAP_FX_s15_expatm_p250 OK (4122s, 553 trades, 51G free)
[2026-10-12T21:01:32Z] [col_1p] ==========================================
[2026-10-12T21:01:32Z] [col_1p] sweep [col_1p] COMPLETE -> data/historical/backtest_reports/s6_col_1p (68min)
[2026-10-12T21:01:32Z] [col_1p] ==========================================
[2026-10-12T21:01:34Z] [col_all3] ==========================================
[2026-10-12T21:01:34Z] [col_all3] sweep [col_all3] -> data/historical/backtest_reports/s6_col_all3 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-12T21:01:34Z] [col_all3] ==========================================
[2026-10-12T21:01:34Z] [col_all3] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activati
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
