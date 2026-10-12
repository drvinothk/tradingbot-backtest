# btsync status  2026-10-12T12:03:18Z UTC / 2026-10-12 17:33:18 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 17:33:18 IST / 12:03:18 UTC  load: 4.91 4.76 4.70  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-082852.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rebase3y_1012.sh"
  backtest-20261012-115331.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_emanotrail_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rb3_orb_chain.heartbeat
2026-10-12 16:42:35 IST rb3_orb: reaper timer stopped
2026-10-12 16:42:37 IST rb3_orb: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rb3_ema_chain.heartbeat
2026-10-12 15:31:23 IST rb3_ema: reaper timer stopped
2026-10-12 15:31:24 IST rb3_ema: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 16:42:35 IST rb3_ema: sweep finished rc=0
2026-10-12 16:42:35 IST rb3_ema: chain finished
-- rgR_c4_chain.heartbeat
2026-10-12 13:45:00 IST rgR_c4: reaper timer stopped
2026-10-12 13:45:02 IST rgR_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:48:28 IST rgR_c4: sweep finished rc=0
2026-10-12 13:48:28 IST rgR_c4: chain finished
2026-10-12 13:48:28 IST rgR_c4: reaper timer restarted
== last 8 s6_status lines:
[2026-10-12T11:12:35Z] [rb3_ema] EMA_FX_r28spec_t05 OK (4271s, 605 trades, 51G free)
[2026-10-12T11:12:35Z] [rb3_ema] ==========================================
[2026-10-12T11:12:35Z] [rb3_ema] sweep [rb3_ema] COMPLETE -> data/historical/backtest_reports/s6_rb3_ema (71min)
[2026-10-12T11:12:35Z] [rb3_ema] ==========================================
[2026-10-12T11:12:37Z] [rb3_orb] ==========================================
[2026-10-12T11:12:37Z] [rb3_orb] sweep [rb3_orb] -> data/historical/backtest_reports/s6_rb3_orb (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T11:12:37Z] [rb3_orb] ==========================================
[2026-10-12T11:12:37Z] [rb3_orb] --- ORB_FX_live (orb_conviction, src=combined_2020) params={"stop_pct": 0.2, "target_pct": 0.66, "trail_activation_fraction": 0.18, "trail_lock_fraction": 0.7, "orb_en
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
