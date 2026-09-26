import sys
p = sys.argv[1]
raw = open(p, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')


def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)


# imports
sub("    compute_fib_levels,\n    resample_multi_day_htf,\n    trend_run_direction,\n)",
    "    compute_fib_levels,\n    ema_side_ok,\n    entry_run_allowed,\n    resample_multi_day_htf,\n    trend_run_direction,\n    trend_run_length,\n)")
# param keys
sub('    "reversal_exit_mode",\n',
    '    "reversal_exit_mode",\n    "flat_exit_candles",\n    "entry_run_rule",\n    "ema_cross_lookback_candles",\n    "ema_candle_position",\n')
# ctor signature
sub('        reversal_exit_mode: str = "static",\n',
    '        reversal_exit_mode: str = "static",\n        flat_exit_candles: int = 0,\n        entry_run_rule: str = "any",\n        ema_cross_lookback_candles: int = 1,\n        ema_candle_position: str = "close",\n')
# validation
sub('''                "engine rebuilds the brick series from one constant brick size"
            )
''', '''                "engine rebuilds the brick series from one constant brick size"
            )
        if flat_exit_candles < 0:
            raise ValueError("flat_exit_candles must be >= 0")
        if flat_exit_candles > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("flat_exit_candles > 0 requires reversal_exit_mode='dynamic'")
        if entry_run_rule not in ("any", "fresh", "fresh_or_cross"):
            raise ValueError(
                f"entry_run_rule must be 'any', 'fresh' or 'fresh_or_cross', "
                f"got {entry_run_rule!r}"
            )
        if entry_run_rule == "fresh_or_cross" and direction_filter_mode != "ema_crossover":
            raise ValueError(
                "entry_run_rule='fresh_or_cross' requires direction_filter_mode='ema_crossover'"
            )
        if ema_cross_lookback_candles < 1:
            raise ValueError("ema_cross_lookback_candles must be >= 1")
        if ema_candle_position not in ("close", "extreme"):
            raise ValueError(
                f"ema_candle_position must be 'close' or 'extreme', got {ema_candle_position!r}"
            )
        if ema_candle_position == "extreme" and (
            direction_filter_mode != "ema_crossover" or entry_mode != "breakout"
        ):
            raise ValueError(
                "ema_candle_position='extreme' requires direction_filter_mode='ema_crossover' "
                "and entry_mode='breakout'"
            )
''')
# attributes
sub("        self.reversal_exit_mode = reversal_exit_mode\n",
    "        self.reversal_exit_mode = reversal_exit_mode\n        self.flat_exit_candles = flat_exit_candles\n        self.entry_run_rule = entry_run_rule\n        self.ema_cross_lookback_candles = ema_cross_lookback_candles\n        self.ema_candle_position = ema_candle_position\n")
# spec
sub('''            "confirm_bricks": int(n),
        }''', '''            "confirm_bricks": int(n),
            "flat_exit_candles": int(self.flat_exit_candles),
        }''')
# check_setup ema block
sub('''            ema_resolved = self._resolve_ema_reference(db, latest_bar, bar_day)
            if ema_resolved is None:
                self._log_once(
                    logger,
                    "ema_not_ready",
                    "run %s: resampled %d-min EMA%d not warmed up yet",
                    strategy_run.id,
                    self.ema_timeframe_minutes,
                    self.ema_period,
                )
                return None
            _, reference_level = ema_resolved
        else:
            reference_level = fib.pob
''', '''            ema_tail = self._resolve_ema_tail(
                db,
                latest_bar,
                bar_day,
                self.ema_cross_lookback_candles + 1
                if self.entry_run_rule == "fresh_or_cross"
                else 1,
            )
            if ema_tail is None:
                self._log_once(
                    logger,
                    "ema_not_ready",
                    "run %s: resampled %d-min EMA%d not warmed up yet",
                    strategy_run.id,
                    self.ema_timeframe_minutes,
                    self.ema_period,
                )
                return None
            reference_level = ema_tail[-1][1]
        else:
            ema_tail = None
            reference_level = fib.pob
''')
sub('''            option_type = self._breakout_signal(new_bricks, trend, close, reference_level)
        else:''', '''            extreme = ema_tail is not None and self.ema_candle_position == "extreme"
            option_type = self._breakout_signal(
                new_bricks,
                trend,
                close,
                reference_level,
                candle_low=ema_tail[-1][0].low if extreme else None,  # type: ignore[index]
                candle_high=ema_tail[-1][0].high if extreme else None,  # type: ignore[index]
            )
        else:''')
sub('''        if self._signal_counts.get(option_type, 0) >= self.max_signals_per_direction:
            return None

        if self.direction_filter_mode == "fib_pob":''', '''        if self._signal_counts.get(option_type, 0) >= self.max_signals_per_direction:
            return None

        if self.entry_run_rule != "any":
            run_length = trend_run_length(self._renko.bricks)
            fresh_cross = (
                self._ema_fresh_cross(ema_tail, option_type == OptionType.CE)
                if ema_tail is not None and self.entry_run_rule == "fresh_or_cross"
                else False
            )
            if not entry_run_allowed(
                self.entry_run_rule, run_length, self.confirm_bricks, fresh_cross
            ):
                self._log_once(
                    logger,
                    "run_not_fresh",
                    "run %s: %s rejected -- brick run of %d is not fresh (entry_run_rule=%s, "
                    "no fresh EMA cross)",
                    strategy_run.id,
                    option_type.value,
                    run_length,
                    self.entry_run_rule,
                )
                return None

        if self.direction_filter_mode == "fib_pob":''')
# _breakout_signal
sub('''        close: float,
        reference_level: float,
    ) -> OptionType | None:
        """Fires on the bar that just printed a brick completing the
        confirmed trend run, provided price already clears `reference_level`
        (Fib POB, or the EMA crossover value -- see `direction_filter_mode`).
        """
        if not new_bricks:
            return None
        latest_direction = new_bricks[-1].direction
        if latest_direction != trend:
            return None
        if latest_direction == "up" and close > reference_level:''', '''        close: float,
        reference_level: float,
        *,
        candle_low: float | None = None,
        candle_high: float | None = None,
    ) -> OptionType | None:
        """Fires on the bar that just printed a brick completing the
        confirmed trend run, provided price already clears `reference_level`
        (Fib POB, or the EMA crossover value -- see `direction_filter_mode`).
        With `candle_low`/`candle_high` supplied (`ema_candle_position=
        "extreme"`) the WHOLE source candle must clear it instead of just the
        close: low above the EMA for a CE, high below it for a PE.
        """
        if not new_bricks:
            return None
        latest_direction = new_bricks[-1].direction
        if latest_direction != trend:
            return None
        if candle_low is not None and candle_high is not None:
            if latest_direction == "up" and candle_low > reference_level:
                return OptionType.CE
            if latest_direction == "down" and candle_high < reference_level:
                return OptionType.PE
            return None
        if latest_direction == "up" and close > reference_level:''')
# ema helpers: replace _resolve_ema_reference tail computation
sub('''        ema_series = compute_ema_series(candles, self.ema_period)
        if not ema_series:
            return None
        return candles[-1].close, ema_series[-1]
''', '''        ema_series = compute_ema_series(candles, self.ema_period)
        if not ema_series:
            return None
        return candles[-1].close, ema_series[-1]

    def _resolve_ema_tail(
        self, db: Session, latest_bar: PriceBar, bar_day: date, k: int
    ) -> list[tuple[Bar, float]] | None:
        """The last `k` resampled candles paired with their EMA value,
        oldest first (fewer than `k` if the EMA has warmed up on fewer --
        callers treat a short list as "no evidence of a prior state").
        `None` if the EMA has not warmed up at all. Same multi-day candle
        window as `_resolve_ema_reference`; the EMA series is aligned to the
        END of the candle list (one value per candle once warmed up).
        """
        since = datetime.combine(bar_day, time.min, tzinfo=IST) - timedelta(
            days=self.ema_lookback_days
        )
        until = latest_bar.bucket_start + timedelta(seconds=60)
        bars_by_day = _fetch_bars_by_day(db, self.instrument_id, self.timeframe, since, until)
        candles = resample_multi_day_htf(
            bars_by_day, self.ema_timeframe_minutes * 60, NORMAL_MARKET_OPEN
        )
        ema_series = compute_ema_series(candles, self.ema_period)
        if not ema_series:
            return None
        n = min(k, len(ema_series))
        return list(zip(candles[-n:], ema_series[-n:], strict=True))

    def _ema_fresh_cross(self, ema_tail: list[tuple[Bar, float]], bullish: bool) -> bool:
        """True if the EMA side condition holds on the newest candle but did
        NOT hold on at least one of the preceding `ema_cross_lookback_candles`
        candles -- i.e. the trend filter itself has only just turned positive
        for this direction (`ema_candle_position` decides what "holds" means).
        No earlier candle available -> False (no evidence of a cross).
        """

        def holds(candle: Bar, ema: float) -> bool:
            return ema_side_ok(
                bullish,
                close=candle.close,
                high=candle.high,
                low=candle.low,
                ema=ema,
                position=self.ema_candle_position,
            )

        newest_candle, newest_ema = ema_tail[-1]
        if not holds(newest_candle, newest_ema):
            return False
        return any(not holds(c, e) for c, e in ema_tail[:-1])
''')
open(p, 'wb').write(s.replace('\n', '\r\n').encode('utf-8') if crlf else s.encode('utf-8'))
print('patched', p, 'crlf', crlf)
