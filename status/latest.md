# btsync status  2026-10-12T07:44:53Z UTC / 2026-10-12 13:14:53 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:14:53 IST / 07:44:53 UTC  load: 4.15 3.00 2.02  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- rgA_orb_chain.heartbeat
2026-10-12 13:11:34 IST rgA_orb: reaper timer stopped
2026-10-12 13:11:35 IST rgA_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- rgA_ema_chain.heartbeat
2026-10-12 13:07:59 IST rgA_ema: reaper timer stopped
2026-10-12 13:08:01 IST rgA_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 13:11:33 IST rgA_ema: sweep finished rc=0
2026-10-12 13:11:33 IST rgA_ema: chain finished
-- rgA_vwap1_chain.heartbeat
2026-10-12 13:03:38 IST rgA_vwap1: reaper timer stopped
2026-10-12 13:03:39 IST rgA_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 13:07:59 IST rgA_vwap1: sweep finished rc=0
2026-10-12 13:07:59 IST rgA_vwap1: chain finished
== last 8 s6_status lines:
[2026-10-12T07:41:33Z] [rgA_ema] EMA_FX_r28spec_t05 OK (212s, 10 trades, 52G free)
[2026-10-12T07:41:33Z] [rgA_ema] ==========================================
[2026-10-12T07:41:33Z] [rgA_ema] sweep [rgA_ema] COMPLETE -> data/historical/backtest_reports/s6_rgA_ema (3min)
[2026-10-12T07:41:33Z] [rgA_ema] ==========================================
[2026-10-12T07:41:35Z] [rgA_orb] ==========================================
[2026-10-12T07:41:35Z] [rgA_orb] sweep [rgA_orb] -> data/historical/backtest_reports/s6_rgA_orb (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T07:41:35Z] [rgA_orb] ==========================================
[2026-10-12T07:41:35Z] [rgA_orb] --- ORB_FX_live (orb_conviction, src=combined_2020) params={"stop_pct": 0.2, "target_pct": 0.66, "trail_activation_fraction": 0.18, "trail_lock_fraction": 0.7, "orb_en
== finished configs (all chains): 569
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
