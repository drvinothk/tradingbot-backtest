# btsync status  2026-10-19T20:26:02Z UTC / 2026-10-20 01:56:02 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-20 01:56:02 IST / 20:26:02 UTC  load: 0.00 0.00 0.00  free: 8G avail  disk: 47G free
== units:
(none running)
== run_backtest procs: 0   reaper timer: active   leaked backtest DBs: 0
== chains (newest heartbeats):
-- par_a1_chain.heartbeat
2026-10-14 18:34:43 IST par_a1: reaper timer stopped
2026-10-14 18:34:45 IST par_a1: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-14 18:36:31 IST par_a1: sweep finished rc=0
2026-10-14 18:36:31 IST par_a1: chain finished
2026-10-14 18:36:31 IST par_a1: reaper timer restarted
-- vc_old_chain.heartbeat
2026-10-14 14:46:39 IST vc_old: reaper timer stopped
2026-10-14 14:46:40 IST vc_old: QC ok; 79 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-14 14:58:14 IST vc_old: sweep finished rc=0
2026-10-14 14:58:14 IST vc_old: chain finished
2026-10-14 14:58:14 IST vc_old: reaper timer restarted
-- vc_new_chain.heartbeat
2026-10-14 14:35:11 IST vc_new: reaper timer stopped
2026-10-14 14:35:13 IST vc_new: QC ok; 79 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-14 14:46:38 IST vc_new: sweep finished rc=0
2026-10-14 14:46:38 IST vc_new: chain finished
2026-10-14 14:46:38 IST vc_new: reaper timer restarted
== last 8 s6_status lines:
[2026-10-14T13:04:45Z] [par_a1] sweep [par_a1] -> data/historical/backtest_reports/s6_par_a1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-14T13:04:45Z] [par_a1] data_through=2026-10-13 pairs=/home/ubuntu/backtest_engine/sweep_configs/pairs_qc16.txt
[2026-10-14T13:04:45Z] [par_a1] ==========================================
[2026-10-14T13:04:45Z] [par_a1] --- EMA_Convic_Paper_Q5Floor_1p1 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_act
[2026-10-14T13:06:31Z] [par_a1] EMA_Convic_Paper_Q5Floor_1p1 OK (106s, 25 trades, 51G free)
[2026-10-14T13:06:31Z] [par_a1] ==========================================
[2026-10-14T13:06:31Z] [par_a1] sweep [par_a1] COMPLETE -> data/historical/backtest_reports/s6_par_a1 (1min)
[2026-10-14T13:06:31Z] [par_a1] ==========================================
== finished configs (all chains): 570
== md5:
a4565279 backend/scripts/run_backtest.py
54526971 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
