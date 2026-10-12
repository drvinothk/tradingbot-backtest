# btsync status  2026-10-12T08:03:02Z UTC / 2026-10-12 13:33:02 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:33:02 IST / 08:03:02 UTC  load: 5.45 4.78 3.77  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 3   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgL_c4_chain.heartbeat
2026-10-12 13:29:47 IST rgL_c4: reaper timer stopped
2026-10-12 13:29:48 IST rgL_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgL_orb_chain.heartbeat
2026-10-12 13:26:18 IST rgL_orb: reaper timer stopped
2026-10-12 13:26:19 IST rgL_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:29:47 IST rgL_orb: sweep finished rc=0
2026-10-12 13:29:47 IST rgL_orb: chain finished
-- rgL_ema_chain.heartbeat
2026-10-12 13:22:46 IST rgL_ema: reaper timer stopped
2026-10-12 13:22:47 IST rgL_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:26:18 IST rgL_ema: sweep finished rc=0
2026-10-12 13:26:18 IST rgL_ema: chain finished
== last 8 s6_status lines:
[2026-10-12T07:59:47Z] [rgL_orb] ORB_FX_live OK (208s, 11 trades, 52G free)
[2026-10-12T07:59:47Z] [rgL_orb] ==========================================
[2026-10-12T07:59:47Z] [rgL_orb] sweep [rgL_orb] COMPLETE -> data/historical/backtest_reports/s6_rgL_orb (3min)
[2026-10-12T07:59:47Z] [rgL_orb] ==========================================
[2026-10-12T07:59:48Z] [rgL_c4] ==========================================
[2026-10-12T07:59:48Z] [rgL_c4] sweep [rgL_c4] -> data/historical/backtest_reports/s6_rgL_c4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-12T07:59:48Z] [rgL_c4] ==========================================
[2026-10-12T07:59:48Z] [rgL_c4] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
