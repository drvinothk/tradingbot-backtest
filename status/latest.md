# btsync status  2026-10-12T08:13:15Z UTC / 2026-10-12 13:43:15 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:43:15 IST / 08:13:15 UTC  load: 5.34 4.47 3.95  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgR_orb_chain.heartbeat
2026-10-12 13:41:07 IST rgR_orb: reaper timer stopped
2026-10-12 13:41:09 IST rgR_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgR_ema_chain.heartbeat
2026-10-12 13:37:32 IST rgR_ema: reaper timer stopped
2026-10-12 13:37:33 IST rgR_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:41:07 IST rgR_ema: sweep finished rc=0
2026-10-12 13:41:07 IST rgR_ema: chain finished
-- rgR_vwap1_chain.heartbeat
2026-10-12 13:33:13 IST rgR_vwap1: reaper timer stopped
2026-10-12 13:33:14 IST rgR_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:37:32 IST rgR_vwap1: sweep finished rc=0
2026-10-12 13:37:32 IST rgR_vwap1: chain finished
== last 8 s6_status lines:
[2026-10-12T08:11:07Z] [rgR_ema] EMA_FX_r28spec_t05 OK (214s, 9 trades, 52G free)
[2026-10-12T08:11:07Z] [rgR_ema] ==========================================
[2026-10-12T08:11:07Z] [rgR_ema] sweep [rgR_ema] COMPLETE -> data/historical/backtest_reports/s6_rgR_ema (3min)
[2026-10-12T08:11:07Z] [rgR_ema] ==========================================
[2026-10-12T08:11:09Z] [rgR_orb] ==========================================
[2026-10-12T08:11:09Z] [rgR_orb] sweep [rgR_orb] -> data/historical/backtest_reports/s6_rgR_orb (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T08:11:09Z] [rgR_orb] ==========================================
[2026-10-12T08:11:09Z] [rgR_orb] --- ORB_FX_live (orb_conviction, src=combined_2020) params={"stop_pct": 0.2, "target_pct": 0.66, "trail_activation_fraction": 0.18, "trail_lock_fraction": 0.7, "orb_en
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
