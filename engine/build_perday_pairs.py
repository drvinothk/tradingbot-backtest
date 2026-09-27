#!/usr/bin/env python3
"""Build the exact `day:expiry` pair list for the PER-DAY backtest harness (2026-09-25).

The default harness (run_sweep_default.sh -> run_sweep_perday.sh) replays every trading day as an isolated
fresh-database `--pairs` run, so each day can trade once. The old `--all-expiries` harness keeps one continuous
run per expiry directory, where the first dispatched position never closes in-DB and risk-blocks the rest of
the week -> ONE trade per expiry week, ~94% of them on the Wednesday (DTE 6) -- see BACKTEST_LEARNINGS.md 2026-09-25.

Rule (same as `--near-expiry-days 6`): each expiry directory E contributes the days D with E-6 <= D <= E that
have option rows in that directory, weekdays only, and that also have underlying (alice_index) 1-min data.
Days whose near-week options are missing (data gaps, e.g. the Diwali week) are simply not in the list.

Usage: build_perday_pairs.py [--underlying NIFTY] [--out sweep_configs/perday_pairs.txt] [--from 2025-08-28] [--to YYYY-MM-DD]
Prints the pair count and the uncovered trading days.
"""
from __future__ import annotations

import argparse
import csv
import os
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
HIST = HERE / "backend" / "data" / "historical"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--underlying", default="NIFTY")
    ap.add_argument("--options-subdir", default="options_1min_past")
    ap.add_argument("--out", default=str(HERE / "sweep_configs" / "perday_pairs.txt"))
    ap.add_argument("--from", dest="d_from", default=None)
    ap.add_argument("--to", dest="d_to", default=None)
    ap.add_argument("--near-expiry-days", type=int, default=6)
    ap.add_argument(
        "--source", default="alice_index",
        help="underlyings/<u>_<source>_1min.csv to check day-coverage against (default alice_index, "
        "unchanged behavior). '2026-09-28: use combined_2020 for any pair-list spanning before "
        "2023-06-13 -- alice_index has zero rows there and would silently drop every such day.",
    )
    a = ap.parse_args()

    und_csv = HIST / "underlyings" / f"{a.underlying}_{a.source}_1min.csv"
    und_days = {ln[:10] for ln in open(und_csv) if ln[:1].isdigit()}
    base = HIST / a.options_subdir / a.underlying
    pairs: dict[str, str] = {}
    for d in sorted(os.listdir(base)):
        exp = date.fromisoformat(d)
        lo = exp - timedelta(days=a.near_expiry_days)
        files = sorted(os.listdir(base / d))
        seen: set[date] = set()
        for f in files[:: max(1, len(files) // 8)]:  # a spread of strikes is enough to find the days present
            with open(base / d / f) as fh:
                r = csv.reader(fh)
                next(r)
                for row in r:
                    x = date.fromisoformat(row[0][:10])
                    if lo <= x <= exp:
                        seen.add(x)
        for x in seen:
            if x.weekday() < 5 and x.isoformat() in und_days:
                pairs[x.isoformat()] = d
    lo_d = a.d_from or min(pairs)
    hi_d = a.d_to or max(und_days)
    kept = {k: v for k, v in sorted(pairs.items()) if lo_d <= k <= hi_d}
    Path(a.out).write_text(",".join(f"{k}:{v}" for k, v in kept.items()))
    unc = sorted(d for d in und_days if lo_d <= d <= hi_d and d not in kept and date.fromisoformat(d).weekday() < 5)
    print(f"{len(kept)} day:expiry pairs {min(kept)} -> {max(kept)} written to {a.out}")
    print(f"{len(unc)} trading days with underlying data but no near-week option data (not tradable in either harness): {unc}")


if __name__ == "__main__":
    main()
