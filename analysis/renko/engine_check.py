import sys,types,csv,glob,os
from datetime import datetime,timedelta
from types import SimpleNamespace
sys.path.insert(0,"C:/Users/drvin/Trading Bot/backtest_engine/backend/scripts")
sys.path.insert(0,"C:/Users/drvin/Trading Bot/backtest_engine/backend")
import run_backtest as rb
from app.domain.strategy.models import SignalSide
import replay as R
H=R.H
ub=rb._load_csv_bars(__import__('pathlib').Path(H+'underlyings/NIFTY_alice_index_1min.csv'))
useries=[(b.ts,b.close) for b in ub]
T=R.load_trades('renko2c/renko2c_b833_r15_current.csv')
def run(spec,struct_level_fn,trail,target_pct,label,rn):
    ok=bad=0; details=[]
    for t in T:
        if t['sym'] not in R.idx or t['e'].date() not in R.Ub: continue
        ev=R.renko_events(t['e'].date(),8.33,15); sb=t['e']-timedelta(minutes=1)
        if sb not in ev: continue
        _,top,bot=ev[sb]
        ep=t['ep']; stop=R.rt(ep*0.65); tgt=R.rt(ep*(1+target_pct))
        lvl=(bot-8.33*rn) if t['ce'] else (top+8.33*rn)
        ti=SimpleNamespace(created_at=datetime.combine(t['e'].date(),t['e'].time(),tzinfo=rb.IST),entry_price=ep,stop_price=stop,target_price=tgt,side=SignalSide.BUY,
            trail_activation_fraction=trail[0],trail_lock_fraction=trail[1],structure_level=lvl,structure_break_buffer=0.15*(R.atr.get(sb) or 0),structure_break_persistence_seconds=6.0)
        bars=[rb.Bar(ts=ts.replace(tzinfo=rb.IST),open=o,high=h,low=l,close=c,volume=0,oi=0) for ts,o,h,l,c in R.obars(t['sym'])]
        otype=rb.DomainOptionType.CE if t['ce'] else rb.DomainOptionType.PE
        r=rb._reconstruct_exit_current(ti,t['sym'],bars,65,1,underlying_series=useries,option_type=otype,renko_dynamic_exit=spec)
        # replay
        if spec: rr=R.simulate(t,8.33,15,struct=(('flat',spec['flat_exit_candles']) if spec.get('flat_exit_candles') else ('dyn',rn)),trail=(0.5,0.6) if trail[0]<5 else None,target_pct=target_pct if target_pct<5 else None)
        else: rr=R.simulate(t,8.33,15,struct=('static',rn))
        m=(rr['x']==r.exit_time.replace(tzinfo=None) and abs(rr['xp']-r.exit_price)<0.06)
        ok+=m; bad+=(not m)
        if not m: details.append((t['sym'],t['e'],r.exit_time,r.exit_price,r.exit_reason,rr))
    print(label,'match',ok,'mismatch',bad)
    for d in details[:5]: print('  ',d)
spec={"brick_size":8.33,"timeframe_minutes":15,"confirm_bricks":1}
run(None,None,(0.5,0.6),0.6,'engine static n=1 vs replay',1)
run(spec,None,(0.5,0.6),0.6,'engine DYNAMIC n=1 (trail+tgt) vs replay',1)
run({**spec,"confirm_bricks":2},None,(0.5,0.6),0.6,'engine DYNAMIC n=2 (trail+tgt) vs replay',2)
run(spec,None,(1000.0,0.6),9.0,'engine DYNAMIC n=1 premium trail/target disabled vs replay',1)
# flat exit parity (reverse-run set unreachable so flat semantics are isolated; replay flat = "no favourable brick")
for k in (1,2,3):
    run({**spec,"confirm_bricks":99,"flat_exit_candles":k},None,(20.0,0.6),9.0,f'engine FLAT k={k} (premium trail/tgt off) vs replay',1)
