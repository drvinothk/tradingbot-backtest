# btsync status  2026-10-12T18:18:43Z UTC / 2026-10-12 23:48:43 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 23:48:43 IST / 18:18:43 UTC  load: 4.64 4.60 4.64  free: 6G avail  disk: 51G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rem_c4t5_chain.heartbeat
2026-10-12 22:42:00 IST rem_c4t5: reaper timer stopped
2026-10-12 22:42:01 IST rem_c4t5: QC ok; 764 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- ngt_colsmoke_chain.heartbeat
2026-10-12 22:41:12 IST ngt_colsmoke: reaper timer stopped
2026-10-12 22:41:13 IST ngt_colsmoke: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 22:42:00 IST ngt_colsmoke: sweep finished rc=0
2026-10-12 22:42:00 IST ngt_colsmoke: chain finished
-- ngt_reg_c4_chain.heartbeat
2026-10-12 22:39:08 IST ngt_reg_c4: reaper timer stopped
2026-10-12 22:39:10 IST ngt_reg_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 22:41:12 IST ngt_reg_c4: sweep finished rc=0
2026-10-12 22:41:12 IST ngt_reg_c4: chain finished
== last 8 s6_status lines:
[2026-10-12T17:12:00Z] [ngt_colsmoke] VWAP_FX_s15_expatm_p250 OK (47s, 5 trades, 52G free)
[2026-10-12T17:12:00Z] [ngt_colsmoke] ==========================================
[2026-10-12T17:12:00Z] [ngt_colsmoke] sweep [ngt_colsmoke] COMPLETE -> data/historical/backtest_reports/s6_ngt_colsmoke (0min)
[2026-10-12T17:12:00Z] [ngt_colsmoke] ==========================================
[2026-10-12T17:12:01Z] [rem_c4t5] ==========================================
[2026-10-12T17:12:01Z] [rem_c4t5] sweep [rem_c4t5] -> data/historical/backtest_reports/s6_rem_c4t5 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-12T17:12:01Z] [rem_c4t5] ==========================================
[2026-10-12T17:12:01Z] [rem_c4t5] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activati
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
