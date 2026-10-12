# btsync status  2026-10-12T08:51:01Z UTC / 2026-10-12 14:21:01 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 14:21:01 IST / 08:51:01 UTC  load: 0.43 0.45 0.75  free: 8G avail  disk: 52G free
== units:
  backtest-20261012-082852.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_rebase3y_1012.sh"
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
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
-- rgR_ema_chain.heartbeat
2026-10-12 13:37:32 IST rgR_ema: reaper timer stopped
2026-10-12 13:37:33 IST rgR_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 13:41:07 IST rgR_ema: sweep finished rc=0
2026-10-12 13:41:07 IST rgR_ema: chain finished
== last 8 s6_status lines:
[2026-10-12T08:15:02Z] [rgR_c4] ==========================================
[2026-10-12T08:15:02Z] [rgR_c4] sweep [rgR_c4] -> data/historical/backtest_reports/s6_rgR_c4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-12T08:15:02Z] [rgR_c4] ==========================================
[2026-10-12T08:15:02Z] [rgR_c4] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
[2026-10-12T08:18:28Z] [rgR_c4] VWAP_FX_s15_expatm_p250 OK (206s, 27 trades, 52G free)
[2026-10-12T08:18:28Z] [rgR_c4] ==========================================
[2026-10-12T08:18:28Z] [rgR_c4] sweep [rgR_c4] COMPLETE -> data/historical/backtest_reports/s6_rgR_c4 (3min)
[2026-10-12T08:18:28Z] [rgR_c4] ==========================================
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
