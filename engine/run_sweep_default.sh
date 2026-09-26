#!/usr/bin/env bash
# DEFAULT sweep entry point (2026-09-25; multi-trade made the default 2026-09-26): the PER-DAY harness. Every trading day is an isolated fresh-DB replay (--pairs), so a
# config can trade once per DAY (~236 trades/yr) instead of once per expiry WEEK (~50, ~94% Wednesday) -- see
# backend/scripts/BACKTEST_LEARNINGS.md 2026-09-25 and README "Run a sweep".
#
#   RUN_TAG=<tag> [SHARD_COUNT=4] ./run_sweep_default.sh <config_file>                  # per-day (default)
#   ONE_TRADE_PER_DAY=1 RUN_TAG=<tag> ./run_sweep_default.sh <config_file>                # first-signal-only per day (biased; quick look) --
#                                                                                        # ONLY when the user explicitly asks for one trade per day
# Default = per-day MULTI-TRADE (a strategy can re-enter after an exit, as live does). The weekly harness is OFF.
# Config format is the canonical one (name|strategy_type|params_json). Runs the same source-resolution + real _build_strategy QC gate
# as run_sweep_canonical.sh, rebuilds the pair list from the data on disk, then hands off to run_sweep_perday.sh.
# Launch it via `sudo /opt/backtest/run_bt.sh ...` like every other sweep (README restrictive rule 1).
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
RUN_TAG="${RUN_TAG:?set RUN_TAG}"
CONFIG_FILE="${1:?usage: run_sweep_default.sh <config_file>}"
[ -f "$CONFIG_FILE" ] || CONFIG_FILE="$HERE/$CONFIG_FILE"
CONFIG_FILE="$(cd "$(dirname "$CONFIG_FILE")" && pwd)/$(basename "$CONFIG_FILE")"   # absolute: the QC step runs from backend/scripts
# The one-trade-per-expiry-WEEK harness is permanently OFF (user decision 2026-09-26): 94% Wednesday-only, it inverted strategy signs.
if [ -n "${HARNESS:-}" ]; then
  echo "HARNESS is no longer supported (weekly harness is OFF). Default = per-day MULTI-TRADE; ONE_TRADE_PER_DAY=1 = per-day first-signal-only."; exit 2
fi
PY="$HERE/backend/.venv/bin/python"
export PAIRS_FILE="${PAIRS_FILE:-$HERE/sweep_configs/perday_pairs.txt}"
"$PY" "$HERE/setup/build_perday_pairs.py" --out "$PAIRS_FILE" || { echo "[$RUN_TAG] pair build FAILED"; exit 1; }
RESOLVED="/tmp/${RUN_TAG}_perday_resolved_$(date +%s).txt"
( cd "$HERE/backend/scripts" && "$PY" resolve_and_qc.py "$CONFIG_FILE" "$RESOLVED" ) || { echo "[$RUN_TAG] QC FAILED -- not launching"; exit 1; }
echo "[$RUN_TAG] PER-DAY harness ($([ "${ONE_TRADE_PER_DAY:-0}" = "1" ] && echo ONE-TRADE-PER-DAY || echo MULTI-TRADE default)), $(tr ',' '\n' < "$PAIRS_FILE" | wc -l) day:expiry pairs, resolved config: $RESOLVED"
[ "${DRY_RUN:-0}" = "1" ] && { echo "[$RUN_TAG] DRY_RUN=1 -- QC + pairs OK, not launching"; exit 0; }
exec "$HERE/run_sweep_perday.sh" "$RESOLVED"
