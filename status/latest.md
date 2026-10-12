# btsync status  2026-10-12T10:54:38Z UTC / 2026-10-12 16:24:38 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 16:24:38 IST / 10:54:38 UTC  load: 4.83 4.84 4.70  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-082852.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rebase3y_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rb3_ema_chain.heartbeat
2026-10-12 15:31:23 IST rb3_ema: reaper timer stopped
2026-10-12 15:31:24 IST rb3_ema: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rgR_c4_chain.heartbeat
2026-10-12 13:45:00 IST rgR_c4: reaper timer stopped
2026-10-12 13:45:02 IST rgR_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:48:28 IST rgR_c4: sweep finished rc=0
2026-10-12 13:48:28 IST rgR_c4: chain finished
2026-10-12 13:48:28 IST rgR_c4: reaper timer restarted
-- rgR_orb_chain.heartbeat
2026-10-12 13:41:07 IST rgR_orb: reaper timer stopped
2026-10-12 13:41:09 IST rgR_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:44:39 IST rgR_orb: sweep finished rc=0
2026-10-12 13:44:39 IST rgR_orb: chain finished
== last 8 s6_status lines:
[2026-10-12T08:18:28Z] [rgR_c4] VWAP_FX_s15_expatm_p250 OK (206s, 27 trades, 52G free)
[2026-10-12T08:18:28Z] [rgR_c4] ==========================================
[2026-10-12T08:18:28Z] [rgR_c4] sweep [rgR_c4] COMPLETE -> data/historical/backtest_reports/s6_rgR_c4 (3min)
[2026-10-12T08:18:28Z] [rgR_c4] ==========================================
[2026-10-12T10:01:24Z] [rb3_ema] ==========================================
[2026-10-12T10:01:24Z] [rb3_ema] sweep [rb3_ema] -> data/historical/backtest_reports/s6_rb3_ema (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-12T10:01:24Z] [rb3_ema] ==========================================
[2026-10-12T10:01:24Z] [rb3_ema] --- EMA_FX_r28spec_t05 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activation_f
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
