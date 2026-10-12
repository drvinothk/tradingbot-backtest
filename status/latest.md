# btsync status  2026-10-12T07:46:03Z UTC / 2026-10-12 13:16:03 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-10-12 13:16:03 IST / 07:46:03 UTC  load: 4.25 3.25 2.18  free: 6G avail  disk: 52G free
== units:
  backtest-20261012-073337.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./regress_fill_1012.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- rgA_c4_chain.heartbeat
2026-10-12 13:15:03 IST rgA_c4: reaper timer stopped
2026-10-12 13:15:04 IST rgA_c4: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
-- rgA_orb_chain.heartbeat
2026-10-12 13:11:34 IST rgA_orb: reaper timer stopped
2026-10-12 13:11:35 IST rgA_orb: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 13:15:03 IST rgA_orb: sweep finished rc=0
2026-10-12 13:15:03 IST rgA_orb: chain finished
-- rgA_ema_chain.heartbeat
2026-10-12 13:07:59 IST rgA_ema: reaper timer stopped
2026-10-12 13:08:01 IST rgA_ema: QC ok; 20 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine ad5984e0
2026-10-12 13:11:33 IST rgA_ema: sweep finished rc=0
2026-10-12 13:11:33 IST rgA_ema: chain finished
== last 8 s6_status lines:
[2026-10-12T07:45:03Z] [rgA_orb] ORB_FX_live OK (208s, 11 trades, 52G free)
[2026-10-12T07:45:03Z] [rgA_orb] ==========================================
[2026-10-12T07:45:03Z] [rgA_orb] sweep [rgA_orb] COMPLETE -> data/historical/backtest_reports/s6_rgA_orb (3min)
[2026-10-12T07:45:03Z] [rgA_orb] ==========================================
[2026-10-12T07:45:04Z] [rgA_c4] ==========================================
[2026-10-12T07:45:04Z] [rgA_c4] sweep [rgA_c4] -> data/historical/backtest_reports/s6_rgA_c4 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --data-dir /home/
[2026-10-12T07:45:04Z] [rgA_c4] ==========================================
[2026-10-12T07:45:04Z] [rgA_c4] --- VWAP_FX_s15_expatm_p250 (vwap_pullback_conviction, src=futures_proxy) params={"pullback_tolerance_frac": 0.001, "max_vwap_crosses_in_lookback": 1, "trail_activation
== finished configs (all chains): 569
== md5:
ad5984e0 backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
