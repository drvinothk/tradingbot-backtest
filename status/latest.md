# btsync status  2026-10-12T13:17:14Z UTC / 2026-10-12 18:47:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 18:47:14 IST / 13:17:14 UTC  load: 4.63 4.66 4.69  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-082852.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rebase3y_1012.sh"
  backtest-20261012-115331.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_emanotrail_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rb3_c4t1_chain.heartbeat
2026-10-12 17:49:41 IST rb3_c4t1: reaper timer stopped
2026-10-12 17:49:43 IST rb3_c4t1: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rb3_orb_chain.heartbeat
2026-10-12 16:42:35 IST rb3_orb: reaper timer stopped
2026-10-12 16:42:37 IST rb3_orb: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 17:49:41 IST rb3_orb: sweep finished rc=0
2026-10-12 17:49:41 IST rb3_orb: chain finished
-- rb3_ema_chain.heartbeat
2026-10-12 15:31:23 IST rb3_ema: reaper timer stopped
2026-10-12 15:31:24 IST rb3_ema: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 16:42:35 IST rb3_ema: sweep finished rc=0
2026-10-12 16:42:35 IST rb3_ema: chain finished
== last 8 s6_status lines:
[2026-10-12T12:19:41Z] [rb3_orb] ORB_FX_live OK (4024s, 362 trades, 51G free)
[2026-10-12T12:19:41Z] [rb3_orb] ==========================================
[2026-10-12T12:19:41Z] [rb3_orb] sweep [rb3_orb] COMPLETE -> data/historical/backtest_reports/s6_rb3_orb (67min)
[2026-10-12T12:19:41Z] [rb3_orb] ==========================================
[2026-10-12T12:19:43Z] [rb3_c4t1] ==========================================
[2026-10-12T12:19:43Z] [rb3_c4t1] sweep [rb3_c4t1] -> data/historical/backtest_reports/s6_rb3_c4t1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-12T12:19:43Z] [rb3_c4t1] ==========================================
[2026-10-12T12:19:43Z] [rb3_c4t1] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activati
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
