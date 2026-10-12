# btsync status  2026-10-12T19:26:14Z UTC / 2026-10-13 00:56:14 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-13 00:56:14 IST / 19:26:14 UTC  load: 4.96 4.77 4.73  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
sort: write failed: 'standard output': Broken pipe
sort: write error
-- rem_vwap1_chain.heartbeat
2026-10-12 23:53:52 IST rem_vwap1: reaper timer stopped
2026-10-12 23:53:54 IST rem_vwap1: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- rem_c4t5_chain.heartbeat
2026-10-12 22:42:00 IST rem_c4t5: reaper timer stopped
2026-10-12 22:42:01 IST rem_c4t5: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 23:53:52 IST rem_c4t5: sweep finished rc=0
2026-10-12 23:53:52 IST rem_c4t5: chain finished
-- ngt_colsmoke_chain.heartbeat
2026-10-12 22:41:12 IST ngt_colsmoke: reaper timer stopped
2026-10-12 22:41:13 IST ngt_colsmoke: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 22:42:00 IST ngt_colsmoke: sweep finished rc=0
2026-10-12 22:42:00 IST ngt_colsmoke: chain finished
== last 8 s6_status lines:
[2026-10-12T18:23:52Z] [rem_c4t5] VWAP_FX_s15_expatm_p250 OK (4311s, 988 trades, 51G free)
[2026-10-12T18:23:52Z] [rem_c4t5] ==========================================
[2026-10-12T18:23:52Z] [rem_c4t5] sweep [rem_c4t5] COMPLETE -> data/historical/backtest_reports/s6_rem_c4t5 (71min)
[2026-10-12T18:23:52Z] [rem_c4t5] ==========================================
[2026-10-12T18:23:54Z] [rem_vwap1] ==========================================
[2026-10-12T18:23:54Z] [rem_vwap1] sweep [rem_vwap1] -> data/historical/backtest_reports/s6_rem_vwap1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-12T18:23:54Z] [rem_vwap1] ==========================================
[2026-10-12T18:23:54Z] [rem_vwap1] --- VWAP_FX_stack_rr12 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
