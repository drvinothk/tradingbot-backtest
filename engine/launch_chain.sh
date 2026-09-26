#!/usr/bin/env bash
# Unattended multi-chunk MULTI-TRADE per-day chain (2026-09-26). Usage (via run_bt.sh, see README):
#   TAG=w12 END_BY_UTC="2026-09-28 02:00:00" ./launch_chain.sh sweep_configs/renko12a_warm_batch.txt sweep_configs/renko12b_warm_batch.txt ...
# Guards: single-instance, reaper stop/restart (trap), engine+script md5 frozen at start (abort between chunks if any changed -- another session
# deployed mid-run), chunk-level QC (rows, tracebacks, shard failures), no NEW chunk if its projected end passes END_BY_UTC (Monday-open guard),
# stop after 2 consecutive failed chunks. Every config runs with --extra-warmup-days 21 (production-like 20-day ATR/EMA history).
set -u
ENGINE=/home/ubuntu/backtest_engine
TAG="${TAG:?set TAG}"
HB=$ENGINE/logs/${TAG}_chain.heartbeat
say() { echo "$(TZ=Asia/Kolkata date "+%Y-%m-%d %H:%M:%S IST") $TAG: $*" | tee -a "$HB"; }
[ $# -ge 1 ] || { echo "no chunk files"; exit 2; }
END_EPOCH=$(date -u -d "${END_BY_UTC:?set END_BY_UTC}" +%s)
if pgrep -f "run_backtest\.py|run_sweep" >/dev/null; then say "ABORT -- a sweep is running (rule 10)"; exit 1; fi
cleanup() { sudo -n systemctl start backtest-reaper.timer && say "reaper timer restarted"; }
sudo -n systemctl stop backtest-reaper.timer && say "reaper timer stopped"
trap cleanup EXIT
cd "$ENGINE" || { say "ABORT cd"; exit 1; }
FILES="backend/scripts/run_backtest.py run_sweep_perday.sh run_sweep_default.sh backend/app/modules/strategy_engine/strategies/renko_trend.py backend/app/modules/strategy_engine/higher_timeframe.py"
SUMS0=$(md5sum $FILES); say "frozen md5s: $(echo "$SUMS0" | awk '{print substr($1,1,8)}' | tr '\n' ' ')"
export MULTI_TRADE=1 SHARD_COUNT="${SHARD_COUNT:-4}" EXTRA_BT_ARGS="--extra-warmup-days 21"
fails=0; done_cfg=0; done_secs=0
for f in "$@"; do
  n=$(grep -cv '^#' "$f"); ctag="${TAG}$(basename "$f" | sed -E 's/^renko[0-9]+([a-z]?)_.*/\1/')"
  [ "$(md5sum $FILES)" = "$SUMS0" ] || { say "ABORT -- engine/scripts changed during the chain"; exit 3; }
  avg=$(( done_cfg > 0 ? done_secs / done_cfg : 4200 ))
  if [ $(( $(date +%s) + n * avg )) -gt "$END_EPOCH" ]; then say "STOP -- $f ($n cfgs x ${avg}s) would end after END_BY_UTC; not started"; break; fi
  say "chunk $ctag: launching $f ($n configs, avg ${avg}s/cfg, SHARD_COUNT=$SHARD_COUNT, extra='$EXTRA_BT_ARGS')"
  t0=$(date +%s)
  RUN_TAG="$ctag" ./run_sweep_default.sh "$f" > "$ENGINE/logs/${ctag}_full.out" 2>&1; rc=$?
  el=$(( $(date +%s) - t0 ))
  ok=$(grep -cE "\[$ctag\] .* OK " "$ENGINE/logs/s6_status.log"); bad=$(grep -cE "\[$ctag\] .*(HAD SHARD FAILURES|merge FAILED)" "$ENGINE/logs/s6_status.log")
  tb=$(cat /tmp/s6_logs/$ctag/*.log 2>/dev/null | grep -c Traceback)
  say "chunk $ctag: rc=$rc ${el}s ok=$ok shard-failures=$bad tracebacks=$tb"
  done_cfg=$(( done_cfg + n )); done_secs=$(( done_secs + el ))
  if [ "$rc" -ne 0 ] || [ "$bad" -gt 0 ]; then fails=$(( fails + 1 )); else fails=0; fi
  [ "$fails" -ge 2 ] && { say "ABORT -- 2 consecutive failed chunks"; exit 4; }
done
say "chain finished ($done_cfg configs run)"
