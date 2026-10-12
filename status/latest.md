# btsync status  2026-10-12T07:59:33Z UTC / 2026-10-12 13:29:33 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:29:33 IST / 07:59:33 UTC  load: 4.70 4.36 3.43  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgL_orb_chain.heartbeat
2026-10-12 13:26:18 IST rgL_orb: reaper timer stopped
2026-10-12 13:26:19 IST rgL_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgL_ema_chain.heartbeat
2026-10-12 13:22:46 IST rgL_ema: reaper timer stopped
2026-10-12 13:22:47 IST rgL_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:26:18 IST rgL_ema: sweep finished rc=0
2026-10-12 13:26:18 IST rgL_ema: chain finished
-- rgL_vwap1_chain.heartbeat
2026-10-12 13:18:27 IST rgL_vwap1: reaper timer stopped
2026-10-12 13:18:29 IST rgL_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:22:46 IST rgL_vwap1: sweep finished rc=0
2026-10-12 13:22:46 IST rgL_vwap1: chain finished
== last 8 s6_status lines:
[2026-10-12T07:56:18Z] [rgL_ema] EMA_FX_r28spec_t05 OK (211s, 10 trades, 52G free)
[2026-10-12T07:56:18Z] [rgL_ema] ==========================================
[2026-10-12T07:56:18Z] [rgL_ema] sweep [rgL_ema] COMPLETE -> data/historical/backtest_reports/s6_rgL_ema (3min)
[2026-10-12T07:56:18Z] [rgL_ema] ==========================================
[2026-10-12T07:56:19Z] [rgL_orb] ==========================================
[2026-10-12T07:56:19Z] [rgL_orb] sweep [rgL_orb] -> data/historical/backtest_reports/s6_rgL_orb (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T07:56:19Z] [rgL_orb] ==========================================
[2026-10-12T07:56:19Z] [rgL_orb] --- ORB_FX_live (orb_conviction, src=combined_2020) params={"stop_pct": 0.2, "target_pct": 0.66, "trail_activation_fraction": 0.18, "trail_lock_fraction": 0.7, "orb_en
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
