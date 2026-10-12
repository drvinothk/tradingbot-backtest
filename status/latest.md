# btsync status  2026-10-12T20:12:24Z UTC / 2026-10-13 01:42:24 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 01:42:24 IST / 20:12:24 UTC  load: 4.63 4.65 4.63  free: 7G avail  disk: 51G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- col_1p_chain.heartbeat
2026-10-13 01:22:49 IST col_1p: reaper timer stopped
2026-10-13 01:22:50 IST col_1p: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- rem_vwap1_chain.heartbeat
2026-10-12 23:53:52 IST rem_vwap1: reaper timer stopped
2026-10-12 23:53:54 IST rem_vwap1: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-13 01:22:49 IST rem_vwap1: sweep finished rc=0
2026-10-13 01:22:49 IST rem_vwap1: chain finished
-- rem_c4t5_chain.heartbeat
2026-10-12 22:42:00 IST rem_c4t5: reaper timer stopped
2026-10-12 22:42:01 IST rem_c4t5: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 23:53:52 IST rem_c4t5: sweep finished rc=0
2026-10-12 23:53:52 IST rem_c4t5: chain finished
== last 8 s6_status lines:
[2026-10-12T19:52:49Z] [rem_vwap1] VWAP_FX_stack_rr12 OK (5335s, 534 trades, 51G free)
[2026-10-12T19:52:49Z] [rem_vwap1] ==========================================
[2026-10-12T19:52:49Z] [rem_vwap1] sweep [rem_vwap1] COMPLETE -> data/historical/backtest_reports/s6_rem_vwap1 (88min)
[2026-10-12T19:52:49Z] [rem_vwap1] ==========================================
[2026-10-12T19:52:50Z] [col_1p] ==========================================
[2026-10-12T19:52:50Z] [col_1p] sweep [col_1p] -> data/historical/backtest_reports/s6_col_1p (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-12T19:52:50Z] [col_1p] ==========================================
[2026-10-12T19:52:50Z] [col_1p] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
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
