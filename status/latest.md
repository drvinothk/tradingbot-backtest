# btsync status  2026-10-11T22:09:30Z UTC / 2026-10-12 03:39:30 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 03:39:30 IST / 22:09:30 UTC  load: 4.82 4.69 4.66  free: 8G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap33_chain.heartbeat
2026-10-12 02:11:00 IST fxvwap33: reaper timer stopped
2026-10-12 02:11:01 IST fxvwap33: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap33s_chain.heartbeat
2026-10-12 02:10:11 IST fxvwap33s: reaper timer stopped
2026-10-12 02:10:12 IST fxvwap33s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 02:11:00 IST fxvwap33s: sweep finished rc=0
2026-10-12 02:11:00 IST fxvwap33s: chain finished
-- fxvwap32_chain.heartbeat
2026-10-11 23:38:52 IST fxvwap32: reaper timer stopped
2026-10-11 23:38:53 IST fxvwap32: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 02:10:10 IST fxvwap32: sweep finished rc=0
2026-10-12 02:10:10 IST fxvwap32: chain finished
== last 8 s6_status lines:
[2026-10-11T20:41:00Z] [fxvwap33s] VWAP_FX_s15_expatm_p250_atr OK (48s, 0 trades, 52G free)
[2026-10-11T20:41:00Z] [fxvwap33s] ==========================================
[2026-10-11T20:41:00Z] [fxvwap33s] sweep [fxvwap33s] COMPLETE -> data/historical/backtest_reports/s6_fxvwap33s (0min)
[2026-10-11T20:41:00Z] [fxvwap33s] ==========================================
[2026-10-11T20:41:01Z] [fxvwap33] ==========================================
[2026-10-11T20:41:01Z] [fxvwap33] sweep [fxvwap33] -> data/historical/backtest_reports/s6_fxvwap33 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir 
[2026-10-11T20:41:01Z] [fxvwap33] ==========================================
[2026-10-11T20:41:01Z] [fxvwap33] --- VWAP_FX_s15_expatm_p250_atr (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_acti
== finished configs (all chains): 567
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
sort: write failed: 'standard output': Broken pipe
sort: write error
ATTENTION: none
```
