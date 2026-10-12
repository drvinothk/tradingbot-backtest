# btsync status  2026-10-12T07:33:39Z UTC / 2026-10-12 13:03:39 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:03:39 IST / 07:33:39 UTC  load: 0.71 0.57 0.62  free: 8G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 0   reaper timer: inactive   leaked backtest DBs: 0
== chains (newest heartbeats):
-- rgA_vwap1_chain.heartbeat
2026-10-12 13:03:38 IST rgA_vwap1: reaper timer stopped
2026-10-12 13:03:39 IST rgA_vwap1: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- fxvwap35_chain.heartbeat
2026-10-12 07:15:51 IST fxvwap35: reaper timer stopped
2026-10-12 07:15:52 IST fxvwap35: QC ok; 1472 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 10:10:48 IST fxvwap35: sweep finished rc=0
2026-10-12 10:10:48 IST fxvwap35: chain finished
-- fxvwap35s_chain.heartbeat
2026-10-12 07:15:02 IST fxvwap35s: reaper timer stopped
2026-10-12 07:15:04 IST fxvwap35s: QC ok; 5 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 07:15:51 IST fxvwap35s: sweep finished rc=0
2026-10-12 07:15:51 IST fxvwap35s: chain finished
== last 8 s6_status lines:
[2026-10-12T04:40:48Z] [fxvwap35] VWAP_FX_s15_expatm_p250_tl3 OK (10496s, 1859 trades, 52G free)
[2026-10-12T04:40:48Z] [fxvwap35] ==========================================
[2026-10-12T04:40:48Z] [fxvwap35] sweep [fxvwap35] COMPLETE -> data/historical/backtest_reports/s6_fxvwap35 (174min)
[2026-10-12T04:40:48Z] [fxvwap35] ==========================================
[2026-10-12T07:33:39Z] [rgA_vwap1] ==========================================
[2026-10-12T07:33:39Z] [rgA_vwap1] sweep [rgA_vwap1] -> data/historical/backtest_reports/s6_rgA_vwap1 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-d
[2026-10-12T07:33:39Z] [rgA_vwap1] ==========================================
[2026-10-12T07:33:39Z] [rgA_vwap1] --- VWAP_FX_stack_rr12 (vwap_pullback_conviction, src=futures_proxy) params={}
== finished configs (all chains): 569
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
