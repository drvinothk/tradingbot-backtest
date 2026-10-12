# btsync status  2026-10-12T07:55:00Z UTC / 2026-10-12 13:25:00 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:25:00 IST / 07:55:00 UTC  load: 4.91 4.06 3.05  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgL_ema_chain.heartbeat
2026-10-12 13:22:46 IST rgL_ema: reaper timer stopped
2026-10-12 13:22:47 IST rgL_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgL_vwap1_chain.heartbeat
2026-10-12 13:18:27 IST rgL_vwap1: reaper timer stopped
2026-10-12 13:18:29 IST rgL_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:22:46 IST rgL_vwap1: sweep finished rc=0
2026-10-12 13:22:46 IST rgL_vwap1: chain finished
-- rgA_c4_chain.heartbeat
2026-10-12 13:15:03 IST rgA_c4: reaper timer stopped
2026-10-12 13:15:04 IST rgA_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 13:18:27 IST rgA_c4: sweep finished rc=0
2026-10-12 13:18:27 IST rgA_c4: chain finished
== last 8 s6_status lines:
[2026-10-12T07:52:46Z] [rgL_vwap1] VWAP_FX_stack_rr12 OK (257s, 19 trades, 52G free)
[2026-10-12T07:52:46Z] [rgL_vwap1] ==========================================
[2026-10-12T07:52:46Z] [rgL_vwap1] sweep [rgL_vwap1] COMPLETE -> data/historical/backtest_reports/s6_rgL_vwap1 (4min)
[2026-10-12T07:52:46Z] [rgL_vwap1] ==========================================
[2026-10-12T07:52:47Z] [rgL_ema] ==========================================
[2026-10-12T07:52:47Z] [rgL_ema] sweep [rgL_ema] -> data/historical/backtest_reports/s6_rgL_ema (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T07:52:47Z] [rgL_ema] ==========================================
[2026-10-12T07:52:47Z] [rgL_ema] --- EMA_FX_r28spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
