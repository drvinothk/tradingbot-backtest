#!/usr/bin/env bash
# PER-DAY variant of run_sweep.sh (2026-09-25): --pairs instead of --all-expiries, so every trading day is an isolated fresh-DB
# replay (one trade per DAY, not per expiry week). Needs PAIRS_FILE. Everything else identical to run_sweep.sh.
# Bundle entry point for running a config sweep.
#
# This is runners/run_phase6_generic.sh adapted to (a) this folder layout and
# (b) a 2-OCPU box. The originals in runners/ are kept UNMODIFIED as provenance
# for the e4 runs already in the ledger -- don't run those here, their relative
# paths and SHARD_COUNT=28 assume the old VM.
#
# Usage:
#   RUN_TAG=g9a EXTRA_BT_ARGS='--structure-stop-mode pivot_s1r1' \
#     ./run_sweep.sh sweep_configs/phase8_groupe_liquidity_entry.txt
#
# Env:
#   RUN_TAG        (required) names the output dir + database suffixes
#   EXTRA_BT_ARGS  extra flags appended to every run_backtest.py invocation
#   SHARD_COUNT    default 4 (A1 has 2 OCPU; the e4 used 28 on 32 vCPU)
#   DB_NAME        default btengine -- must match backend/.env
#   MIN_FREE_GB    default 15 -- sweep aborts below this
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
# Pause switch (2026-09-26): while $HERE/STOP_PERDAY exists, no NEW per-day config is started (a config already running finishes normally).
if [ -e "$HERE/STOP_PERDAY" ]; then echo "[perday] STOP_PERDAY flag present -- not starting $(basename "${1:-}")"; exit 0; fi
cd "$HERE/backend"

PY=./.venv/bin/python
PSQL="${PSQL:-sudo -u postgres psql}"
SHARD_COUNT="${SHARD_COUNT:-4}"
PAIRS="$(cat "${PAIRS_FILE:?set PAIRS_FILE}")"   # per-day harness: exact day:expiry pairs, each an isolated fresh-DB replay
RUN_TAG="${RUN_TAG:?set RUN_TAG}"
EXTRA_BT_ARGS="${EXTRA_BT_ARGS:-}"
# 2026-09-26 (user decision): MULTI-TRADE IS THE DEFAULT. Each replayed position is closed at its reconstructed exit so a strategy can
# trade more than once a day (run_backtest.py --multi-trade; needs --exit-mode current, which this script always passes). The
# first-signal-only ("one trade per day", biased) variant runs ONLY when explicitly requested: ONE_TRADE_PER_DAY=1.
if [ "${ONE_TRADE_PER_DAY:-0}" = "1" ]; then
  HARNESS_LABEL="ONE-TRADE-PER-DAY (first signal only; biased, explicit request)"
else
  HARNESS_LABEL="MULTI-TRADE per day (default)"
  EXTRA_BT_ARGS="$EXTRA_BT_ARGS --multi-trade"
fi
DB_NAME="${DB_NAME:-btengine}"
MIN_FREE_GB="${MIN_FREE_GB:-15}"
DB_PREFIX="${DB_NAME}_backtest_s6_${RUN_TAG}_"
RESULTS_DIR="data/historical/backtest_reports/s6_${RUN_TAG}"
STATUS_FILE="$HERE/logs/s6_status.log"
LOG_DIR="/tmp/s6_logs/${RUN_TAG}"
CONFIG_FILE="${1:?usage: run_sweep.sh <config_list_file>}"
[ -f "$CONFIG_FILE" ] || CONFIG_FILE="$HERE/$CONFIG_FILE"

mkdir -p "$RESULTS_DIR" "$LOG_DIR" "$HERE/logs"
log() { echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] [$RUN_TAG] $*" | tee -a "$STATUS_FILE"; }

reap_dbs() {
  $PSQL -tAc "SELECT 'DROP DATABASE IF EXISTS \"'||datname||'\" WITH (FORCE);'
    FROM pg_database WHERE datname ~ '^${DB_PREFIX}'" 2>/dev/null | $PSQL -q 2>/dev/null || true
}
trap reap_dbs EXIT

"$HERE/setup/disk_guard.sh" "$MIN_FREE_GB" || exit 1

n_configs=$(grep -cv '^#' "$CONFIG_FILE")
log "=========================================="
log "sweep [$RUN_TAG] -> $RESULTS_DIR ($n_configs configs, ${SHARD_COUNT} shards) harness=$HARNESS_LABEL extra='$EXTRA_BT_ARGS'"
log "=========================================="
sweep_start=$(date +%s)

while IFS='|' read -r name strategy_type source params; do
  [ -z "$name" ] && continue
  case "$name" in \#*) continue ;; esac
  cfg_start=$(date +%s)
  log "--- $name ($strategy_type, src=$source) params=$params"

  pids=()
  for i in $(seq 0 $((SHARD_COUNT - 1))); do
    "$PY" scripts/run_backtest.py \
      --strategy "$strategy_type" --underlying NIFTY \
      --pairs "$PAIRS" --options-subdir options_1min_past \
      --underlying-source "$source" \
      --exit-mode current --fast \
      --strategy-params "$params" \
      $EXTRA_BT_ARGS \
      --shard-count "$SHARD_COUNT" --shard-index "$i" \
      --db-suffix "s6_${RUN_TAG}_${name}_s${i}" \
      --out-csv "${RESULTS_DIR}/${name}_s${i}.csv" \
      > "${LOG_DIR}/${name}_s${i}.log" 2>&1 &
    pids+=($!)
  done

  fail=0
  for pid in "${pids[@]}"; do wait "$pid" || fail=1; done

  "$PY" scripts/merge_backtest_shards.py \
    --glob "${RESULTS_DIR}/${name}_s*.csv" \
    --out "${RESULTS_DIR}/${name}_current.csv" \
    >> "${LOG_DIR}/${name}_merge.log" 2>&1 || log "*** $name merge FAILED"

  reap_dbs

  el=$(( $(date +%s) - cfg_start ))
  n=$(( $(wc -l < "${RESULTS_DIR}/${name}_current.csv" 2>/dev/null || echo 1) - 1 ))
  free=$(df -h --output=avail / | tail -1 | tr -d ' ')
  log "$name $([ $fail -eq 0 ] && echo OK || echo 'HAD SHARD FAILURES') (${el}s, ${n} trades, ${free} free)"
done < "$CONFIG_FILE"

log "=========================================="
log "sweep [$RUN_TAG] COMPLETE -> $RESULTS_DIR ($(( ($(date +%s) - sweep_start) / 60 ))min)"
log "=========================================="
