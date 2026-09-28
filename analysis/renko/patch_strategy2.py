import sys

WT = "D:/tb-renko-fix/backend/app/modules/strategy_engine/"


def load(p):
    raw = open(p, 'rb').read()
    return raw.decode('utf-8').replace('\r\n', '\n'), (b'\r\n' in raw)


def save(p, s, crlf):
    open(p, 'wb').write((s.replace('\n', '\r\n') if crlf else s).encode('utf-8'))


# ---------------- renko.py ----------------
p = WT + "renko.py"
s, crlf = load(p)


def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)


sub('''    "RenkoState",
    "compute_fib_levels",
''', '''    "RenkoState",
    "compute_fib_levels",
    "count_direction_flips",
''')
sub('''    "entry_run_allowed",
    "resample_multi_day_htf",
''', '''    "entry_run_allowed",
    "move_from_open_ok",
    "resample_multi_day_htf",
''')
sub('''def entry_run_allowed(
    rule: str,''', '''def count_direction_flips(bricks: list[RenkoBrick]) -> int:
    """Number of direction changes between adjacent bricks (0 for < 2
    bricks). `min_flips_today` (2026-09-24) uses it as a day-context measure:
    0 = a one-way day so far (an entry now is an established-trend chase),
    >= 1 = price has already turned at least once today.
    """
    return sum(1 for a, b in zip(bricks, bricks[1:], strict=False) if a.direction != b.direction)


def move_from_open_ok(bullish: bool, close: float, day_open: float, max_move_points: float) -> bool:
    """`max_move_from_open_points` gate (2026-09-24), the anti-chase filter:
    how far price has already travelled from the day's open IN THE TRADE'S
    DIRECTION (up for a CE, down for a PE). A move against the trade (negative)
    always passes; the entry is refused only once the favourable move already
    exceeds `max_move_points`.
    """
    move = (close - day_open) if bullish else (day_open - close)
    return move <= max_move_points


def entry_run_allowed(
    rule: str,''')
save(p, s, crlf)
print('renko.py patched')

# ---------------- renko_trend.py ----------------
p = WT + "strategies/renko_trend.py"
s, crlf = load(p)

sub("    compute_fib_levels,\n    ema_side_ok,\n", "    compute_fib_levels,\n    count_direction_flips,\n    ema_side_ok,\n")
sub("    entry_run_allowed,\n    resample_multi_day_htf,\n", "    entry_run_allowed,\n    move_from_open_ok,\n    resample_multi_day_htf,\n")
sub('    "ema_candle_position",\n    "entry_start_time",\n', '    "ema_candle_position",\n    "no_progress_exit_candles",\n    "allowed_directions",\n    "max_move_from_open_points",\n    "min_flips_today",\n    "entry_start_time",\n')
sub('        ema_candle_position: str = "close",\n        entry_start_time',
    '        ema_candle_position: str = "close",\n        no_progress_exit_candles: int = 0,\n        allowed_directions: str = "both",\n        max_move_from_open_points: float | None = None,\n        min_flips_today: int = 0,\n        entry_start_time')
sub('''        if direction_filter_mode not in ("fib_pob", "ema_crossover"):
            raise ValueError(
                f"direction_filter_mode must be 'fib_pob' or 'ema_crossover', "
                f"got {direction_filter_mode!r}"
            )
''', '''        if direction_filter_mode not in ("fib_pob", "ema_crossover", "none"):
            raise ValueError(
                f"direction_filter_mode must be 'fib_pob', 'ema_crossover' or 'none', "
                f"got {direction_filter_mode!r}"
            )
        if direction_filter_mode == "none" and entry_mode != "breakout":
            raise ValueError("direction_filter_mode='none' requires entry_mode='breakout'")
''')
sub('''        self.entry_start_time = _parse_hhmm(entry_start_time)
''', '''        self.no_progress_exit_candles = no_progress_exit_candles
        self.allowed_directions = allowed_directions
        self.max_move_from_open_points = max_move_from_open_points
        self.min_flips_today = min_flips_today
        self.entry_start_time = _parse_hhmm(entry_start_time)
''')
sub('''        self.entry_cutoff_time = _parse_hhmm(entry_cutoff_time)

''', '''        self.entry_cutoff_time = _parse_hhmm(entry_cutoff_time)

''')  # anchor sanity
sub('''        if reversal_exit_mode == "dynamic" and not exit_on_reversal:''', '''        if no_progress_exit_candles < 0:
            raise ValueError("no_progress_exit_candles must be >= 0")
        if no_progress_exit_candles > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("no_progress_exit_candles > 0 requires reversal_exit_mode='dynamic'")
        if allowed_directions not in ("both", "ce", "pe"):
            raise ValueError(
                f"allowed_directions must be 'both', 'ce' or 'pe', got {allowed_directions!r}"
            )
        if max_move_from_open_points is not None and max_move_from_open_points <= 0:
            raise ValueError("max_move_from_open_points must be > 0 when set")
        if min_flips_today < 0:
            raise ValueError("min_flips_today must be >= 0")
        if reversal_exit_mode == "dynamic" and not exit_on_reversal:''')
sub('''        self._signal_counts: dict[OptionType, int] = {}

    def _brick_size_band''', '''        self._signal_counts: dict[OptionType, int] = {}
        self._day_open: float | None = None

    def _brick_size_band''')
sub('''        self._signal_counts = {}
        self._logged_keys = set()''', '''        self._signal_counts = {}
        self._day_open = None
        self._logged_keys = set()''')
sub('''            "flat_exit_candles": int(self.flat_exit_candles),
        }''', '''            "flat_exit_candles": int(self.flat_exit_candles),
            "no_progress_exit_candles": int(self.no_progress_exit_candles),
        }''')
# direction filter none
sub('''            reference_level = ema_tail[-1][1]
        else:
            ema_tail = None
            reference_level = fib.pob
''', '''            reference_level = ema_tail[-1][1]
        elif self.direction_filter_mode == "none":
            ema_tail = None
            reference_level = 0.0  # unused -- no reference level in "none" mode
        else:
            ema_tail = None
            reference_level = fib.pob
''')
sub('''        if self.entry_mode == "breakout":
            extreme = ema_tail is not None and self.ema_candle_position == "extreme"
            option_type = self._breakout_signal(
                new_bricks,
                trend,
                close,
                reference_level,
                candle_low=ema_tail[-1][0].low if extreme else None,  # type: ignore[index]
                candle_high=ema_tail[-1][0].high if extreme else None,  # type: ignore[index]
            )
        else:''', '''        if self.entry_mode == "breakout" and self.direction_filter_mode == "none":
            option_type = self._brick_only_signal(new_bricks, trend)
        elif self.entry_mode == "breakout":
            extreme = ema_tail is not None and self.ema_candle_position == "extreme"
            option_type = self._breakout_signal(
                new_bricks,
                trend,
                close,
                reference_level,
                candle_low=ema_tail[-1][0].low if extreme else None,  # type: ignore[index]
                candle_high=ema_tail[-1][0].high if extreme else None,  # type: ignore[index]
            )
        else:''')
sub('''        if option_type is None:
            return None

        if self._signal_counts.get(option_type, 0) >= self.max_signals_per_direction:
            return None
''', '''        if option_type is None:
            return None

        if self.allowed_directions != "both" and option_type.value.lower() != self.allowed_directions:
            self._log_once(
                logger,
                f"direction_not_allowed_{option_type.value}",
                "run %s: %s rejected -- allowed_directions=%s",
                strategy_run.id,
                option_type.value,
                self.allowed_directions,
            )
            return None

        if self._signal_counts.get(option_type, 0) >= self.max_signals_per_direction:
            return None
''')
sub('''        if self.direction_filter_mode == "fib_pob":
            ema_ok: bool | None = self._ema_filter_ok(db, latest_bar, bar_day, option_type)''', '''        if self.max_move_from_open_points is not None:
            day_open = self._resolve_day_open(db, latest_bar, bar_day)
            if day_open is None:
                return None
            if not move_from_open_ok(
                option_type == OptionType.CE, close, day_open, self.max_move_from_open_points
            ):
                self._log_once(
                    logger,
                    f"move_from_open_{option_type.value}",
                    "run %s: %s rejected -- already moved > %.0f pts from the day's open %.2f "
                    "(close %.2f)",
                    strategy_run.id,
                    option_type.value,
                    self.max_move_from_open_points,
                    day_open,
                    close,
                )
                return None

        if self.min_flips_today > 0:
            flips = count_direction_flips(self._renko.bricks)
            if flips < self.min_flips_today:
                self._log_once(
                    logger,
                    f"too_few_flips_{option_type.value}",
                    "run %s: %s rejected -- only %d direction flip(s) in today's bricks "
                    "(min_flips_today=%d)",
                    strategy_run.id,
                    option_type.value,
                    flips,
                    self.min_flips_today,
                )
                return None

        if self.direction_filter_mode == "fib_pob":
            ema_ok: bool | None = self._ema_filter_ok(db, latest_bar, bar_day, option_type)''')
sub('''    def _pullback_signal(''', '''    def _brick_only_signal(
        self, new_bricks: list[RenkoBrick], trend: BrickDirection
    ) -> OptionType | None:
        """`direction_filter_mode="none"`: no reference level at all -- fires
        on the bar that just printed a brick completing the confirmed run,
        CE for an up-run, PE for a down-run. The control arm for measuring
        what the EMA guidance is worth.
        """
        if not new_bricks or new_bricks[-1].direction != trend:
            return None
        return OptionType.CE if trend == "up" else OptionType.PE

    def _resolve_day_open(
        self, db: Session, latest_bar: PriceBar, bar_day: date
    ) -> float | None:
        """Open of the day's first 1-minute bar (the 09:15 open), cached for
        the day. `None` (and no entry) if the day has no bars yet."""
        if self._day_open is None:
            day_start = datetime.combine(bar_day, NORMAL_MARKET_OPEN, tzinfo=IST)
            bars = get_recent_completed_bars(
                db,
                self.instrument_id,
                self.timeframe,
                since=day_start,
                until=latest_bar.bucket_start + timedelta(seconds=60),
            )
            if not bars:
                return None
            self._day_open = float(bars[0].open)
        return self._day_open

    def _pullback_signal(''')
save(p, s, crlf)
print('renko_trend.py patched, crlf', crlf)
