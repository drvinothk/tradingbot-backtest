# btsync status  2026-10-12T17:11:30Z UTC / 2026-10-12 22:41:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 22:41:30 IST / 17:11:30 UTC  load: 4.15 4.02 4.44  free: 7G avail  disk: 52G free
== units:
  backtest-20261012-165208.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_night_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- ngt_colsmoke_chain.heartbeat
2026-10-12 22:41:12 IST ngt_colsmoke: reaper timer stopped
2026-10-12 22:41:13 IST ngt_colsmoke: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
-- ngt_reg_c4_chain.heartbeat
2026-10-12 22:39:08 IST ngt_reg_c4: reaper timer stopped
2026-10-12 22:39:10 IST ngt_reg_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 214a0c09
2026-10-12 22:41:12 IST ngt_reg_c4: sweep finished rc=0
2026-10-12 22:41:12 IST ngt_reg_c4: chain finished
-- rb3_ema_nt_chain.heartbeat
2026-10-12 21:28:33 IST rb3_ema_nt: reaper timer stopped
2026-10-12 21:28:34 IST rb3_ema_nt: QC ok; 707 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 10912b27
2026-10-12 22:38:10 IST rb3_ema_nt: sweep finished rc=0
2026-10-12 22:38:10 IST rb3_ema_nt: chain finished
2026-10-12 22:38:10 IST rb3_ema_nt: reaper timer restarted
== last 8 s6_status lines:
[2026-10-12T17:11:12Z] [ngt_reg_c4] VWAP_FX_s15_expatm_p250 OK (122s, 27 trades, 52G free)
[2026-10-12T17:11:12Z] [ngt_reg_c4] ==========================================
[2026-10-12T17:11:12Z] [ngt_reg_c4] sweep [ngt_reg_c4] COMPLETE -> data/historical/backtest_reports/s6_ngt_reg_c4 (2min)
[2026-10-12T17:11:12Z] [ngt_reg_c4] ==========================================
[2026-10-12T17:11:13Z] [ngt_colsmoke] ==========================================
[2026-10-12T17:11:13Z] [ngt_colsmoke] sweep [ngt_colsmoke] -> data/historical/backtest_reports/s6_ngt_colsmoke (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12
[2026-10-12T17:11:13Z] [ngt_colsmoke] ==========================================
[2026-10-12T17:11:13Z] [ngt_colsmoke] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_acti
== finished configs (all chains): 570
== md5:
214a0c09 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
