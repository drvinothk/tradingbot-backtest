# btsync status  2026-10-11T20:40:59Z UTC / 2026-10-12 02:10:59 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 02:10:59 IST / 20:40:59 UTC  load: 3.81 4.49 4.69  free: 10G avail  disk: 52G free
== units:
  backtest-20261011-180803.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_c5_1011.sh"
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- fxvwap33s_chain.heartbeat
2026-10-12 02:10:11 IST fxvwap33s: reaper timer stopped
2026-10-12 02:10:12 IST fxvwap33s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap32_chain.heartbeat
2026-10-11 23:38:52 IST fxvwap32: reaper timer stopped
2026-10-11 23:38:53 IST fxvwap32: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 02:10:10 IST fxvwap32: sweep finished rc=0
2026-10-12 02:10:10 IST fxvwap32: chain finished
-- fxvwap32s_chain.heartbeat
2026-10-11 23:38:03 IST fxvwap32s: reaper timer stopped
2026-10-11 23:38:05 IST fxvwap32s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-11 23:38:52 IST fxvwap32s: sweep finished rc=0
2026-10-11 23:38:52 IST fxvwap32s: chain finished
== last 8 s6_status lines:
[2026-10-11T20:40:10Z] [fxvwap32] VWAP_FX_s15_atm_p250 OK (9077s, 1760 trades, 52G free)
[2026-10-11T20:40:10Z] [fxvwap32] ==========================================
[2026-10-11T20:40:10Z] [fxvwap32] sweep [fxvwap32] COMPLETE -> data/historical/backtest_reports/s6_fxvwap32 (151min)
[2026-10-11T20:40:10Z] [fxvwap32] ==========================================
[2026-10-11T20:40:12Z] [fxvwap33s] ==========================================
[2026-10-11T20:40:12Z] [fxvwap33s] sweep [fxvwap33s] -> data/historical/backtest_reports/s6_fxvwap33s (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-11T20:40:12Z] [fxvwap33s] ==========================================
[2026-10-11T20:40:12Z] [fxvwap33s] --- VWAP_FX_s15_expatm_p250_atr (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_act
== finished configs (all chains): 566
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
! shard/merge failure in s6_status.log within the last 30h:
[2026-10-10T14:51:33Z] [fxvwap21] VWAP_FX_f15_log HAD SHARD FAILURES (8636s, 2477 trades, 54G free)
sort: write failed: 'standard output': Broken pipe
sort: write error
```
