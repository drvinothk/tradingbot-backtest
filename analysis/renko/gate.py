import json
from datetime import time, timedelta
import replay as R
def sim(t,B,tf,base,armed_n,arm='any'):
    """candle exit: adverse-close run >= base normally, >= armed_n while 'armed' by an adverse tf-brick.
    arm='any': armed from first adverse brick since entry; 'cur': armed only while latest brick is adverse (disarms on a favourable brick);
    'flip': armed when net favourable bricks since entry < 0 (below entry level)."""
    day=t['e'].date(); ev=R.renko_events(day,B,tf); ce=t['ce']; fav='up' if ce else 'down'
    armed=False; last=None; net=0; arun=0; lastbar=None
    for ts,o,h,l,c in R.obars(t['sym']):
        if ts<t['e']: continue
        lastbar=(ts,c)
        if ts.time()>=time(15,9): return ts,c
        if ts in ev:
            for d in ev[ts][0]:
                net+=1 if d==fav else -1; last=d
                if arm=='any' and d!=fav: armed=True
                if arm=='cur': armed=(d!=fav)
                if arm=='flip': armed=(net<0)
        cu=R.U.get(ts); pu=R.U.get(ts-timedelta(minutes=1))
        if cu is not None and pu is not None:
            adv=cu[3]<pu[3] if ce else cu[3]>pu[3]
            arun=arun+1 if adv else 0
            need=armed_n if armed else base
            if arun>=need: return ts,c
        else: arun=0
    return lastbar if lastbar else (None,None)
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def run(T,B,tf,*a,**k):
    P=[]
    for t in T:
        x,xp=sim(t,B,tf,*a,**k)
        if x is not None: P.append((xp-t['ep'])*t['qty'])
    h=len(P)//2
    return f"net={sum(P):>7,.0f} PF={pf(P):4.2f} WR={100*sum(x>0 for x in P)/len(P):2.0f}% ex2={sum(sorted(P)[:-2]):>7,.0f} H1={sum(P[:h]):>6,.0f} H2={sum(P[h:]):>6,.0f}"
P={}
for f in ('../../sweep_configs/renko5_overnight_batch.txt','../../sweep_configs/renko6_candle_exit5_batch.txt'):
    for l in open(f):
        if l.startswith('#') or not l.strip(): continue
        n,_,p=l.strip().split('|',2); P[n]=json.loads(p)
CFG=['renko6_tf5_x5_ema15tf','renko6_tf5_x5','renko6_c5_x5_e5','renko6_c4_x5_e5','renko5_b625_mv50ext','renko5_b833_mv50']
V=[('ref cexit5 (no renko)',999,999,'any'),
   ('base5, armed3 (any)',5,3,'any'),('base5, armed2 (any)',5,2,'any'),('base5, armed3 (cur)',5,3,'cur'),('base5, armed4 (cur)',5,4,'cur'),
   ('base8, armed3 (any)',8,3,'any'),('base8, armed5 (any)',8,5,'any'),('base8, armed3 (cur)',8,3,'cur'),
   ('AND-any N3 (base off)',99,3,'any'),('AND-any N4',99,4,'any'),('AND-any N5',99,5,'any'),
   ('AND-cur N3',99,3,'cur'),('AND-cur N5',99,5,'cur'),('AND-flip N3',99,3,'flip'),('AND-flip N5',99,5,'flip')]
for n in CFG:
    p=P[n]; B=p['fixed_brick_size_points']; tf=p['brick_source_timeframe_minutes']
    d='renko6' if n.startswith('renko6') else 'renko5'
    T=sorted([t for t in R.load_trades(f'{d}/{n}_current.csv') if t['sym'] in R.idx and t['e'].date() in R.Ub],key=lambda t:t['e'])
    print(f'\n=== {n[7:]} (tf={tf}, n={len(T)})')
    for lab,b,a,m in V:
        if lab.startswith('ref'):
            print(f' {lab:24}', run(T,B,tf,5,5,'any') if False else run(T,B,tf,5,5,'any'))
        else: print(f' {lab:24}', run(T,B,tf,b,a,m))
