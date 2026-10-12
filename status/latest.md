# btsync status  2026-10-12T15:01:43Z UTC / 2026-10-12 20:31:43 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 20:31:44 IST / 15:01:44 UTC  load: 4.47 4.66 4.70  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-082852.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rebase3y_1012.sh"
  backtest-20261012-115331.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_emanotrail_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rb3_vwap1_chain.heartbeat
2026-10-12 20:05:44 IST rb3_vwap1: reaper timer stopped
2026-10-12 20:05:45 IST rb3_vwap1: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rb3_c4t5_chain.heartbeat
2026-10-12 18:58:09 IST rb3_c4t5: reaper timer stopped
2026-10-12 18:58:10 IST rb3_c4t5: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 20:05:44 IST rb3_c4t5: sweep finished rc=0
2026-10-12 20:05:44 IST rb3_c4t5: chain finished
-- rb3_c4t1_chain.heartbeat
2026-10-12 17:49:41 IST rb3_c4t1: reaper timer stopped
2026-10-12 17:49:43 IST rb3_c4t1: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 18:58:09 IST rb3_c4t1: sweep finished rc=0
2026-10-12 18:58:09 IST rb3_c4t1: chain finished
== last 8 s6_status lines:
[2026-10-12T14:35:44Z] [rb3_c4t5] VWAP_FX_s15_expatm_p250 OK (4054s, 910 trades, 51G free)
[2026-10-12T14:35:44Z] [rb3_c4t5] ==========================================
[2026-10-12T14:35:44Z] [rb3_c4t5] sweep [rb3_c4t5] COMPLETE -> data/historical/backtest_reports/s6_rb3_c4t5 (67min)
[2026-10-12T14:35:44Z] [rb3_c4t5] ==========================================
[2026-10-12T14:35:45Z] [rb3_vwap1] ==========================================
[2026-10-12T14:35:45Z] [rb3_vwap1] sweep [rb3_vwap1] -> data/historical/backtest_reports/s6_rb3_vwap1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-12T14:35:45Z] [rb3_vwap1] ==========================================
[2026-10-12T14:35:45Z] [rb3_vwap1] --- VWAP_FX_stack_rr12 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
