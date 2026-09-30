# btsync status  2026-09-30T13:23:31Z UTC / 2026-09-30 18:53:31 IST  (refreshed every 30 min, on ATTENTION change, and after commands)
```
== now: 2026-09-30 18:53:31 IST / 13:23:31 UTC  load: 4.27 4.54 4.66  free: 8G avail  disk: 62G free
== units:
  backtest-20260930-100731.service loaded active running /bin/bash -c "cd /home/ubuntu/backtest_engine && ./chain_vwap_sep.sh"
== run_backtest procs: 4   reaper timer: inactive   leaked backtest DBs: 4
== chains (newest heartbeats):
-- r29_chain.heartbeat
2026-09-30 18:52:52 IST r29: reaper timer stopped
2026-09-30 18:52:54 IST r29: QC ok; 19 day:expiry pairs, 1 config(s), SHARD_COUNT=4, engine 53208abd
-- vwap_sep_chain.heartbeat
2026-09-30 15:37:31 IST vwap_sep: waiting for the EMA chain (backtest-20260930-061007.service) and any other sweep to finish
2026-09-30 18:52:52 IST vwap_sep: box free
2026-09-30 18:52:52 IST vwap_sep: reaper timer stopped for the chain
2026-09-30 18:52:52 IST vwap_sep: start r29 (VWAP_Base)
-- final_select_chain.heartbeat
2026-09-30 11:40:07 IST final_select: start r27 (EMA_Base_Q5Floor_TSL)
2026-09-30 16:00:00 IST final_select: r27 done (rc=0)
2026-09-30 16:00:00 IST final_select: start r28 (EMA_Convic_Paper_Q5Floor_1p1)
2026-09-30 18:52:32 IST final_select: r28 done (rc=0)
2026-09-30 18:52:32 IST final_select: reaper timer restarted
2026-09-30 18:52:32 IST final_select: chain finished
== last 8 s6_status lines:
[2026-09-30T13:22:32Z] [r28] EMA_Convic_Paper_Q5Floor_1p1 OK (10350s, 1789 trades, 62G free)
[2026-09-30T13:22:32Z] [r28] ==========================================
[2026-09-30T13:22:32Z] [r28] sweep [r28] COMPLETE -> data/historical/backtest_reports/s6_r28 (172min)
[2026-09-30T13:22:32Z] [r28] ==========================================
[2026-09-30T13:22:54Z] [r29] ==========================================
[2026-09-30T13:22:54Z] [r29] sweep [r29] -> data/historical/backtest_reports/s6_r29 (1 configs, 4 shards) harness=MULTI-TRADE per day (default) extra='--extra-warmup-days 12 --multi-trade'
[2026-09-30T13:22:54Z] [r29] ==========================================
[2026-09-30T13:22:54Z] [r29] --- VWAP_Base (vwap_pullback, src=futures_proxy) params={"exit_legs": [{"kind": "core", "qty_fraction": 0.5, "use_structure": true, "trail_lock_fraction": 0.5, "trail_acti
== finished configs (all chains): 506
== md5:
53208abd backend/scripts/run_backtest.py
c8da7ba7 run_sweep_perday.sh
0bb606be run_sweep_default.sh
6a26192c launch_chain.sh
== ATTENTION:
ATTENTION: none
```
