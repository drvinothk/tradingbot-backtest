#!/usr/bin/env python3
"""Canonical sweep-config resolver + QC gate (2026-09-05).

Single source of truth for the one thing that just caused a real, wasted
sweep launch: which `--underlying-source` a strategy_type must use. Built
after `phase13_exit_staging` was first launched with `futures_proxy` for
every config -- wrong for everything except vwap_pullback(_conviction),
caught only because `a_pdt_w65`'s trade count (9) didn't match the
well-established n=26 for that exact entry gate.

Reads a 3-field config file (`name|strategy_type|params_json` -- no source
column, so there is nothing to mistype or forget) and writes a resolved
4-field file (`name|strategy_type|source|params_json`) that
`run_phase6_generic.sh` already knows how to consume unchanged.

A 4th field IS still accepted on input as a deliberate override (e.g. a
genuine one-off "what if I ran ORB on futures_proxy" test) -- printed
loudly as OVERRIDE, never silently accepted, so it's visible in the log
either way.

Also injects `oi_use_futures_volume_confirmation: false` /
`oi_use_atm_oi_buildup: false` for any oi_volume_confirmed* config that
doesn't already set them (the single-snapshot-per-run backtest can't
support the temporal confirmation modes -- BACKTEST_LEARNINGS.md's
canonical-setup section, "always run with" -- both already match the real
class defaults, so this is a no-op belt-and-suspenders, not a behavior
change).

Exits non-zero and prints every failing line if ANY config fails to build
via the real `_build_strategy` -- the caller (`run_sweep_canonical.sh`)
must never launch shards on a QC failure.

Usage:
    ./.venv/bin/python scripts/resolve_and_qc.py <in_config> <out_resolved>
"""
from __future__ import annotations

import json
import sys
import uuid
from datetime import date
from pathlib import Path

sys.path.insert(0, ".")
from app.api.v1.strategies import _build_strategy  # noqa: E402

# Single source of truth -- confirmed against the real canonical baselines
# (d_pdt_w65 / e_pdt_atr / o3_atr_pcrl all alice_index; every VWAP conviction
# config futures_proxy -- see phase4_configs.txt + BACKTEST_LEARNINGS.md's
# "CANONICAL RELIABLE-BACKTEST SETUP" section). Extend this, don't guess a
# new strategy_type's source from an old driver script again.
SOURCE_MAP = {
    "orb": "alice_index",
    "orb_conviction": "alice_index",
    "ema_micro_pullback": "alice_index",
    "ema_micro_pullback_conviction": "alice_index",
    "oi_volume_confirmed": "alice_index",
    "oi_volume_confirmed_conviction": "alice_index",
    "liquidity_sweep_reversal": "alice_index",
    "liquidity_sweep_reversal_conviction": "alice_index",
    "synthetic": "alice_index",
    "atr_breakout": "alice_index",
    "vwap_pullback": "futures_proxy",
    "vwap_pullback_conviction": "futures_proxy",
    # 2026-09-15: new intraday (5-min+) trend-continuation strategies (see
    # higher_timeframe.py's module docstring in the pinned app/ snapshot).
    # id_orb_trend/id_ema_supertrend have no VWAP dependency (breakout+ATR,
    # EMA+Supertrend respectively) -- same source as orb/ema_micro_pullback.
    # id_vwap_continuation needs real volume for VWAP to form at all --
    # same reason vwap_pullback(_conviction) is futures_proxy above.
    "id_orb_trend": "alice_index",
    "id_vwap_continuation": "futures_proxy",
    "id_ema_supertrend": "alice_index",
    # 2026-09-22: Modified Renko trend-following strategy -- price-action
    # only (brick series + Fib/POB off the underlying spot), same reasoning
    # as orb/atr_breakout/id_ema_supertrend above, no VWAP/volume dependency.
    "renko_trend": "alice_index",
}

OI_TYPES = {"oi_volume_confirmed", "oi_volume_confirmed_conviction"}
OI_DEFAULTS = {"oi_use_futures_volume_confirmation": False, "oi_use_atm_oi_buildup": False}


class _Stub:
    def __init__(self, strategy_type: str, params: dict) -> None:
        self.strategy_type = strategy_type
        self.params = params
        self.underlying_symbol = "NIFTY"
        self.interval_seconds = 30
        self.runtime_mode = None


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: resolve_and_qc.py <in_config> <out_resolved>", file=sys.stderr)
        raise SystemExit(2)
    in_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])

    resolved_lines: list[str] = []
    failures: list[str] = []
    unmapped: list[str] = []

    for lineno, raw in enumerate(in_path.read_text().splitlines(), start=1):
        line = raw.rstrip()
        if not line or line.startswith("#"):
            resolved_lines.append(raw)
            continue
        parts = line.split("|", 3)
        if len(parts) == 3:
            name, stype, params_json = parts
            override = None
        elif len(parts) == 4:
            name, stype, override, params_json = parts
        else:
            failures.append(f"line {lineno}: expected 3 or 4 '|'-fields, got {len(parts)}: {line!r}")
            continue

        canonical_source = SOURCE_MAP.get(stype)
        if canonical_source is None:
            unmapped.append(f"line {lineno} ({name}): strategy_type {stype!r} has no SOURCE_MAP entry -- add one, don't guess")
            continue

        if override:
            source = override
            if override != canonical_source:
                print(f"OVERRIDE {name}: using source={override!r}, canonical for {stype} is {canonical_source!r}")
        else:
            source = canonical_source

        params = json.loads(params_json)
        if stype in OI_TYPES:
            for k, v in OI_DEFAULTS.items():
                params.setdefault(k, v)

        try:
            _build_strategy(_Stub(stype, params), uuid.uuid4(), date.today())
        except Exception as exc:  # noqa: BLE001
            failures.append(f"line {lineno} ({name}, {stype}): {type(exc).__name__}: {exc}")
            continue

        resolved_lines.append(f"{name}|{stype}|{source}|{json.dumps(params)}")

    if unmapped:
        print(f"\n{len(unmapped)} UNMAPPED strategy_type(s) -- add to SOURCE_MAP before running:")
        for u in unmapped:
            print(f"  {u}")
    if failures:
        print(f"\n{len(failures)} config(s) FAILED _build_strategy:")
        for f in failures:
            print(f"  {f}")
    if unmapped or failures:
        print("\nQC FAILED -- nothing written, nothing will launch.")
        raise SystemExit(1)

    out_path.write_text("\n".join(resolved_lines) + "\n")
    n = sum(1 for line in resolved_lines if line and not line.startswith("#"))
    print(f"QC OK -- {n} configs resolved + validated -> {out_path}")


if __name__ == "__main__":
    main()
