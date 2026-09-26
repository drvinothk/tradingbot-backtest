import sys, json, uuid, inspect
from datetime import date
sys.path.insert(0, "C:/Users/drvin/Trading Bot/backtest_engine/backend")
from app.api.v1 import strategies as S
from app.domain.strategy.models import StrategyConfig
cfgfile = sys.argv[1]
ok = 0
for line in open(cfgfile):
    if line.startswith('#') or not line.strip(): continue
    name, typ, p = line.strip().split('|', 2); params = json.loads(p)
    unk = S.unrecognised_param_keys(params)
    cfg = StrategyConfig(name=name, strategy_type=typ, params=params)
    try:
        st = S._build_strategy(cfg, uuid.uuid4(), date(2026, 9, 24))
    except Exception as e:
        print('BUILD FAIL', name, repr(e)); continue
    # every param actually reached the object?
    miss = [k for k, v in params.items() if hasattr(st, k) and getattr(st, k) != v and not (k == 'entry_start_time')]
    spec = st.dynamic_reversal_exit_spec
    print(f"OK {name:24} unrecognised={unk} not_applied={miss} noprog={st.no_progress_exit_candles} dirs={st.allowed_directions} mv={st.max_move_from_open_points} flips={st.min_flips_today} mode={st.direction_filter_mode} ema_tf={st.ema_timeframe_minutes} start={st.entry_start_time} spec={spec}")
    ok += 1
print('built', ok)
