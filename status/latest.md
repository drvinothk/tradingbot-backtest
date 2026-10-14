# btsync status  2026-10-14T13:05:14Z UTC / 2026-10-14 18:35:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-14 18:35:14 IST / 13:05:14 UTC  load: 1.86 0.69 0.28  free: 7G avail  disk: 51G free
== units:
  backtest-20261014-130443.service loaded active running /home/ubuntu/backtest_engine/./launch_config_run.sh par_a1 sweep_configs/ema_convic_paper_q5f
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- par_a1_chain.heartbeat
2026-10-14 18:34:43 IST par_a1: reaper timer stopped
2026-10-14 18:34:45 IST par_a1: QC ok; 15 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
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
[2026-10-14T09:28:14Z] [vc_old] ==========================================
[2026-10-14T09:28:14Z] [vc_old] sweep [vc_old] COMPLETE -> data/historical/backtest_reports/s6_vc_old (11min)
[2026-10-14T09:28:14Z] [vc_old] ==========================================
[2026-10-14T13:04:45Z] [par_a1] ==========================================
[2026-10-14T13:04:45Z] [par_a1] sweep [par_a1] -> data/historical/backtest_reports/s6_par_a1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-10-14T13:04:45Z] [par_a1] data_through=2026-10-13 pairs=/home/ubuntu/backtest_engine/sweep_configs/pairs_qc16.txt
[2026-10-14T13:04:45Z] [par_a1] ==========================================
[2026-10-14T13:04:45Z] [par_a1] --- EMA_Convic_Paper_Q5Floor_1p1 (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_act
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
81d4fcc0 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
