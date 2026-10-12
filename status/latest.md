# btsync status  2026-10-12T22:34:44Z UTC / 2026-10-13 04:04:44 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 04:04:44 IST / 22:34:44 UTC  load: 4.45 4.58 4.67  free: 8G avail  disk: 51G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- col_tri_chain.heartbeat
2026-10-13 03:39:26 IST col_tri: reaper timer stopped
2026-10-13 03:39:27 IST col_tri: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- col_all3_chain.heartbeat
2026-10-13 02:31:32 IST col_all3: reaper timer stopped
2026-10-13 02:31:34 IST col_all3: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 03:39:26 IST col_all3: sweep finished rc=0
2026-10-13 03:39:26 IST col_all3: chain finished
-- col_1p_chain.heartbeat
2026-10-13 01:22:49 IST col_1p: reaper timer stopped
2026-10-13 01:22:50 IST col_1p: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 02:31:32 IST col_1p: sweep finished rc=0
2026-10-13 02:31:32 IST col_1p: chain finished
== last 8 s6_status lines:
[2026-10-12T22:09:26Z] [col_all3] VWAP_FX_s15_expatm_p250 OK (4072s, 434 trades, 51G free)
[2026-10-12T22:09:26Z] [col_all3] ==========================================
[2026-10-12T22:09:26Z] [col_all3] sweep [col_all3] COMPLETE -> data/historical/backtest_reports/s6_col_all3 (67min)
[2026-10-12T22:09:26Z] [col_all3] ==========================================
[2026-10-12T22:09:27Z] [col_tri] ==========================================
[2026-10-12T22:09:27Z] [col_tri] sweep [col_tri] -> data/historical/backtest_reports/s6_col_tri (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /ho
[2026-10-12T22:09:27Z] [col_tri] ==========================================
[2026-10-12T22:09:27Z] [col_tri] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activatio
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
