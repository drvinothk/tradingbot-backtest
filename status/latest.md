# btsync status  2026-10-12T08:05:19Z UTC / 2026-10-12 13:35:19 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:35:19 IST / 08:05:19 UTC  load: 4.81 4.71 3.89  free: 6G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgR_vwap1_chain.heartbeat
2026-10-12 13:33:13 IST rgR_vwap1: reaper timer stopped
2026-10-12 13:33:14 IST rgR_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgL_c4_chain.heartbeat
2026-10-12 13:29:47 IST rgL_c4: reaper timer stopped
2026-10-12 13:29:48 IST rgL_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:33:12 IST rgL_c4: sweep finished rc=0
2026-10-12 13:33:12 IST rgL_c4: chain finished
-- rgL_orb_chain.heartbeat
2026-10-12 13:26:18 IST rgL_orb: reaper timer stopped
2026-10-12 13:26:19 IST rgL_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:29:47 IST rgL_orb: sweep finished rc=0
2026-10-12 13:29:47 IST rgL_orb: chain finished
== last 8 s6_status lines:
[2026-10-12T08:03:12Z] [rgL_c4] VWAP_FX_s15_expatm_p250 OK (204s, 24 trades, 52G free)
[2026-10-12T08:03:12Z] [rgL_c4] ==========================================
[2026-10-12T08:03:12Z] [rgL_c4] sweep [rgL_c4] COMPLETE -> data/historical/backtest_reports/s6_rgL_c4 (3min)
[2026-10-12T08:03:12Z] [rgL_c4] ==========================================
[2026-10-12T08:03:14Z] [rgR_vwap1] ==========================================
[2026-10-12T08:03:14Z] [rgR_vwap1] sweep [rgR_vwap1] -> data/historical/backtest_reports/s6_rgR_vwap1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-12T08:03:14Z] [rgR_vwap1] ==========================================
[2026-10-12T08:03:14Z] [rgR_vwap1] --- VWAP_FX_stack_rr12 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
