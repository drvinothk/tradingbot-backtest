import json
from datetime import time, timedelta
import replay as R, bricks as BR
P={}
for f in ('../../sweep_configs/renko5_overnight_batch.txt','../../sweep_configs/renko6_candle_exit5_batch.txt','../../sweep_configs/renko7_entry_batch.txt'):
    for line in open(f):
        if line.startswith('#') or not line.strip(): continue
        n,_,p=line.strip().split('|',2); P[n]=json.loads(p)
CFG={'BASE tf5_x5_ema15tf':('renko6','renko6_tf5_x5_ema15tf'),'MV50 b625_mv50ext':('renko5','renko5_b625_mv50ext'),'E4 tf5_b1000':('renko7','renko7_e4_tf5_b1000')}
def sim(t,B,tf,trail=None,**kw):
    """bricks.sim plus an optional premium trail overlay trail=(act_pct, lock); first exit wins."""
    x,xp,why=BR.sim(t,B,tf,**kw)
    if not trail or x is None: return x,xp,why
    ep=t['ep']; act=ep*(1+trail[0]); ts_=None
    for ts,o,h,l,c in R.obars(t['sym']):
        if ts<t['e']: continue
        if ts>=x: break
        if h>=act:
            new=act+(h-act)*trail[1]
            if ts_ is None or new>ts_: ts_=new
            if l<ts_: return ts,ts_,'trail'
    return x,xp,why
def mdd(p):
    c=pk=d=0
    for a in p: c+=a; pk=max(pk,c); d=max(d,pk-c)
    return d
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def run(T,B,tf,**kw):
    P_=[]
    for t in T:
        x,xp,why=sim(t,B,tf,**kw)
        if x is None: continue
        P_.append(((xp-t['ep'])*t['qty'],t['ce']))
    p=[a for a,_ in P_]; h=len(p)//2; w=[a for a in p if a>0]; l=[a for a in p if a<0]
    return (f"n={len(p):2} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*len(w)/len(p):2.0f}% avgW={sum(w)/len(w):>5,.0f} avgL={sum(l)/len(l):>6,.0f} DD={mdd(p):>6,.0f} ex2={sum(sorted(p)[:-2]):>7,.0f} "
            f"CE={sum(a for a,c in P_ if c):>6,.0f} PE={sum(a for a,c in P_ if not c):>6,.0f} H1={sum(p[:h]):>6,.0f} H2={sum(p[h:]):>6,.0f}")
V=[('cexit 4',dict(rev_early=30,rev_late=30,cexit=4)),('cexit 5',dict(rev_early=30,rev_late=30,cexit=5)),('cexit 6',dict(rev_early=30,rev_late=30,cexit=6)),
   ('cexit 7',dict(rev_early=30,rev_late=30,cexit=7)),('cexit 8',dict(rev_early=30,rev_late=30,cexit=8)),('cexit 10',dict(rev_early=30,rev_late=30,cexit=10)),
   ('brick rev1',dict()),('brick rev2',dict(rev_early=2,rev_late=2)),
   ('cexit5+rev1',dict(cexit=5)),('cexit7+rev1',dict(cexit=7)),
   ('cexit5+noprog4',dict(rev_early=30,rev_late=30,cexit=5,noprog=4)),('cexit5+BE3',dict(rev_early=30,rev_late=30,cexit=5,be_at=3)),
   ('cexit5+tgt10br',dict(rev_early=30,rev_late=30,cexit=5,target=10))]
for pct in (0.3,0.5,0.8):
    for lock in (0.5,0.7):
        V.append((f'cexit5+trail{int(pct*100)}/{lock}',dict(rev_early=30,rev_late=30,cexit=5,trail=(pct,lock))))
        V.append((f'cexit7+trail{int(pct*100)}/{lock}',dict(rev_early=30,rev_late=30,cexit=7,trail=(pct,lock))))
for name,(d,cn) in CFG.items():
    p=P[cn]; B=p['fixed_brick_size_points']; tf=p['brick_source_timeframe_minutes']
    allT=R.load_trades(f'{d}/{cn}_current.csv')
    T=sorted([t for t in allT if t['sym'] in R.idx and t['e'].date() in R.Ub],key=lambda t:t['e'])
    print(f"\n=== {name} B={B} tf={tf} | replay {len(T)}/{len(allT)} trades | engine net {sum(t['pnl'] for t in allT):,.0f}")
    for lab,kw in V: print(f" {lab:20}",run(T,B,tf,**kw))
