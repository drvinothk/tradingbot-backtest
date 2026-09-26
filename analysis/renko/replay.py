"""Offline paired exit replay for renko_trend entries (mirrors run_backtest._reconstruct_exit_current
step order: EOD, stop, target, structure, trail) + a dynamic Renko-brick exit variant."""
import csv,glob,os,bisect
from datetime import datetime,timedelta,time
from decimal import Decimal,ROUND_HALF_UP
from collections import defaultdict
H="C:/Users/drvin/Trading Bot/backtest_engine/backend/data/historical/"
def rt(p,t=0.05): return float((Decimal(str(p))/Decimal(str(t))).to_integral_value(rounding=ROUND_HALF_UP)*Decimal(str(t)))
U={}  # label-> (o,h,l,c)
Ub=defaultdict(list)
for r in csv.DictReader(open(H+'underlyings/NIFTY_alice_index_1min.csv')):
    ts=datetime.fromisoformat(r['timestamp']); v=tuple(float(r[k]) for k in('open','high','low','close')); U[ts]=v; Ub[ts.date()].append(ts)
for d in Ub: Ub[d].sort()
Ukeys=sorted(U); 
def ucl(ts):
    i=bisect.bisect_right(Ukeys,ts)-1
    return U[Ukeys[i]][3] if i>=0 else None
# Wilder ATR14 continuous
atr={}; prev=None; vals=[]; a=None
for ts in Ukeys:
    o,h,l,c=U[ts]; tr=(h-l) if prev is None else max(h-l,abs(h-prev),abs(l-prev)); prev=c
    if a is None:
        vals.append(tr)
        if len(vals)>=14: a=sum(vals)/14
    else: a=(a*13+tr)/14
    atr[ts]=a
idx={os.path.basename(p)[:-4]:p for p in glob.glob(H+'options_1min_past/*/*/*.csv')}
_oc={}
def obars(sym):
    if sym not in _oc:
        _oc[sym]=sorted((datetime.fromisoformat(x['timestamp']),float(x['open']),float(x['high']),float(x['low']),float(x['close'])) for x in csv.DictReader(open(idx[sym])))
    return _oc[sym]
class RS:
    def __init__(s,anchor,B): s.B=B; s.bottom=round(anchor/B)*B; s.top=s.bottom+B
    def update(s,c):
        out=[]
        while c>=s.top+s.B: s.bottom=s.top; s.top+=s.B; out.append('up')
        while c<=s.bottom-s.B: s.top=s.bottom; s.bottom-=s.B; out.append('down')
        return out
_rc={}
def renko_events(day,B,tf):
    k=(day,B,tf)
    if k in _rc: return _rc[k]
    ev={}; st=None; a0=datetime.combine(day,time(9,15))
    for ts in Ub[day]:
        if ((ts-a0).total_seconds()+60)%(tf*60)!=0: continue
        c=U[ts][3]
        if st is None: st=RS(c,B)
        new=st.update(c); ev[ts]=(new,st.top,st.bottom)
    _rc[k]=ev; return ev
def load_trades(path):
    out=[]
    for r in csv.DictReader(open(path)):
        out.append(dict(sym=r['symbol'],ce=r['symbol'].endswith('CE'),e=datetime.fromisoformat(r['entry_time']).replace(tzinfo=None),ep=float(r['entry_price']),
                        x=datetime.fromisoformat(r['exit_time']).replace(tzinfo=None),xp=float(r['exit_price']),reason=r['exit_reason'],pnl=float(r['pnl']),qty=int(r['qty_lots'])*int(r['lot_size'])))
    return out
def simulate(t,B,tf,stop_pct=0.35,target_pct=0.60,trail=(0.5,0.6),struct=None,persist_bars=2,buf_mult=0.15):
    """struct: None | ('static',n) | ('dyn',n)"""
    day=t['e'].date(); ep=t['ep']; ce=t['ce']
    if t['sym'] not in idx or day not in Ub: return None
    sb=t['e']-timedelta(minutes=1); ev=renko_events(day,B,tf)
    if sb not in ev:
        prior=[k for k in ev if k<=sb]   # non-boundary signal (pullback entries): state as of the latest boundary
        if not prior: return dict(err='no boundary before signal')
        sb=max(prior)
    _,top,bot=ev[sb]
    stop=rt(ep*(1-stop_pct)); target=rt(ep*(1+target_pct)) if target_pct is not None else 1e18
    act_price=None; trail_stop=None
    if trail: act_price=ep+abs(target-ep)*trail[0] if target_pct is not None else ep*(1+trail[2])  # trail[2] optional abs activation pct when no target
    level=None
    if struct and struct[0]=='static': level=(bot-struct[1]*B) if ce else (top+struct[1]*B)
    buf=buf_mult*(atr.get(sb) or 0)
    cand=None; run=0
    for ts,o,h,l,c in obars(t['sym']):
        if ts<t['e']: continue
        if ts.time()>=time(15,9): return dict(x=ts,xp=c,reason='eod_square_off')
        if l<=stop: return dict(x=ts,xp=stop,reason='stop')
        if h>=target: return dict(x=ts,xp=target,reason='target')
        if struct:
            if struct[0]=='static':
                u=ucl(ts); bl=level-buf if ce else level+buf
                br=(u<bl) if ce else (u>bl)
                if br:
                    if cand is None: cand=ts
                    if (ts-cand).total_seconds()>=6: return dict(x=ts,xp=c,reason='structure_break')
                else: cand=None
            elif struct[0]=='dyn':
                if ts in ev:
                    for d in ev[ts][0]:
                        rev=(d=='down') if ce else (d=='up')
                        run=run+1 if rev else 0
                        if run>=struct[1]: return dict(x=ts,xp=c,reason='brick_reversal')
            else:  # ('flat',k[,rev_n]): exit after k consecutive source candles printing NO favourable brick (a reverse brick also counts as 'no favourable')
                if ts in ev:
                    favdir='up' if ce else 'down'
                    if favdir in ev[ts][0]: run=0
                    else: run+=1
                    if run>=struct[1]: return dict(x=ts,xp=c,reason='flat_exit')
        if trail:
            if ts.time()<time(15,9):
                fav=h
                if fav>=act_price:
                    ts_new=act_price+(fav-act_price)*trail[1]
                    if trail_stop is None or ts_new>trail_stop: trail_stop=ts_new
                    if l<trail_stop: return dict(x=ts,xp=trail_stop,reason='trail')
    return dict(x=None,xp=None,reason='no_exit')
def pnl(t,r): return (r['xp']-t['ep'])*t['qty']
