#!/usr/bin/env bash
# renko10 MULTI-TRADE per-day batch (2026-09-26): stop reaper, run the 6 configs via run_sweep_default.sh (MULTI_TRADE=1), restart reaper.
set -u
ENGINE=/home/ubuntu/backtest_engine
HB=$ENGINE/logs/mt1_chain.heartbeat
say() { echo "$(TZ=Asia/Kolkata date "+%Y-%m-%d %H:%M:%S IST") mt1: $*" | tee -a "$HB"; }
if pgrep -f "run_backtest\.py|run_sweep" >/dev/null; then say "ABORT -- a sweep is running (rule 10)"; exit 1; fi
sudo -n systemctl stop backtest-reaper.timer && say "reaper timer stopped"
cd "$ENGINE" || { say "ABORT cd"; exit 1; }
say "launching renko10 multi-trade per-day (6 configs, SHARD_COUNT=4)"
MULTI_TRADE=1 RUN_TAG=mt1 SHARD_COUNT=4 ./run_sweep_default.sh sweep_configs/renko10_mt_batch.txt > "$ENGINE/logs/mt1_chain_full.out" 2>&1
say "batch finished rc=$? -- $(grep -cE "\[mt1\] renko10_[a-z0-9_]+ OK " "$ENGINE/logs/s6_status.log") OK (cumulative), $(grep -cE "HAD SHARD FAILURES" "$ENGINE/logs/mt1_chain_full.out") with failures"
sudo -n systemctl start backtest-reaper.timer && say "reaper timer restarted"
