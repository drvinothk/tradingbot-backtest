# btsync status  2026-10-12T16:40:23Z UTC / 2026-10-12 22:10:23 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 22:10:23 IST / 16:40:23 UTC  load: 4.61 4.64 4.64  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-115331.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_emanotrail_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rb3_ema_nt_chain.heartbeat
2026-10-12 21:28:33 IST rb3_ema_nt: reaper timer stopped
2026-10-12 21:28:34 IST rb3_ema_nt: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
-- rb3_vwap1_chain.heartbeat
2026-10-12 20:05:44 IST rb3_vwap1: reaper timer stopped
2026-10-12 20:05:45 IST rb3_vwap1: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 21:28:29 IST rb3_vwap1: sweep finished rc=0
2026-10-12 21:28:29 IST rb3_vwap1: chain finished
-- rb3_c4t5_chain.heartbeat
2026-10-12 18:58:09 IST rb3_c4t5: reaper timer stopped
2026-10-12 18:58:10 IST rb3_c4t5: QC ok; 709 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 20:05:44 IST rb3_c4t5: sweep finished rc=0
2026-10-12 20:05:44 IST rb3_c4t5: chain finished
== last 8 s6_status lines:
[2026-10-12T15:58:29Z] [rb3_vwap1] VWAP_FX_stack_rr12 OK (4964s, 542 trades, 52G free)
[2026-10-12T15:58:29Z] [rb3_vwap1] ==========================================
[2026-10-12T15:58:29Z] [rb3_vwap1] sweep [rb3_vwap1] COMPLETE -> data/historical/backtest_reports/s6_rb3_vwap1 (82min)
[2026-10-12T15:58:29Z] [rb3_vwap1] ==========================================
[2026-10-12T15:58:34Z] [rb3_ema_nt] ==========================================
[2026-10-12T15:58:34Z] [rb3_ema_nt] sweep [rb3_ema_nt] -> data/historical/backtest_reports/s6_rb3_ema_nt (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --mul
[2026-10-12T15:58:34Z] [rb3_ema_nt] ==========================================
[2026-10-12T15:58:34Z] [rb3_ema_nt] --- EMA_FX_r28spec_notrail (ema_micro_pullback_conviction, src=combined_2020) params={"stop_pct": 0.08, "target_pct": 0.12, "trail_lock_fraction": 0.6, "trail_activ
== finished configs (all chains): 569
== md5:
10912b27 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
