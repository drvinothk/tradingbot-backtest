import glob, os, itertools, json
import replay as R, bricks as BR
from datetime import timedelta
P={}
for f in ('../../sweep_configs/renko5_overnight_batch.txt','../../sweep_configs/renko6_candle_exit5_batch.txt'):
    for l in open(f):
        if l.startswith('#') or not l.strip(): continue
        n,_,p=l.strip().split('|',2); P[n]=json.loads(p)
files={os.path.basename(f)[:-12]:f for f in glob.glob('renko5/*_current.csv')+glob.glob('renko6/*_current.csv')}
T={n:R.load_trades(f) for n,f in files.items()}
# 1 exit reasons across all
import collections
rs=collections.Counter(t['reason'] for v in T.values() for t in v); print('exit reasons all 20:',dict(rs))
# 2 entry-set overlap among top configs
top=['renko6_tf5_x5_ema15tf','renko6_tf5_x5','renko5_b625_mv50ext','renko6_c5_x5_e5','renko6_c4_x5_e5','renko5_b833_mv50','renko5_b625_mv40']
S={n:{(t['sym'],t['e']) for t in T[n]} for n in top}
print('entry-set overlap (shared/min n):')
for a,b in itertools.combinations(top,2): print(f'  {a[7:]:16} {b[7:]:16} {len(S[a]&S[b])}/{min(len(S[a]),len(S[b]))}')
allsets={frozenset(s) for s in (frozenset((t['sym'],t['e']) for t in v) for v in T.values())}
print('distinct entry sets among 20 configs:',len(allsets))
# 3 costs sensitivity
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9
print('net after per-trade cost () / concentration:')
for n in top:
    p=[t['pnl'] for t in T[n]]; s=sorted(p,reverse=True)
    print(f'  {n[7:]:16} gross={sum(p):>7,.0f} c150={sum(p)-150*len(p):>7,.0f} c300={sum(p)-300*len(p):>7,.0f} top5share={sum(s[:5])/sum(p):.2f} ex5={sum(s[5:]):>7,.0f} avgprem={sum(t["ep"] for t in T[n])/len(T[n]):.0f} avg_pnl/trade={sum(p)/len(p):.0f} median={sorted(p)[len(p)//2]:.0f}')
# 4 replay vs engine trade-by-trade (cexit5 control), and missing trades
print('replay control vs engine, per trade:')
for n,rev in (('renko6_tf5_x5_ema15tf',1),('renko6_tf5_x5',1),('renko6_c5_x5_e5',1),('renko5_b625_mv50ext',0)):
    p=P[n]; B=p['fixed_brick_size_points']; tf=p['brick_source_timeframe_minutes']; same=diff=miss=0; dd=[]; missp=0
    for t in T[n]:
        if t['sym'] not in R.idx or t['e'].date() not in R.Ub: miss+=1; missp+=t['pnl']; continue
        kw=dict(rev_early=30,rev_late=30,cexit=5) if rev else {}
        x,xp,why=BR.sim(t,B,tf,**kw)
        if x==t['x'] and abs(xp-t['xp'])<0.01: same+=1
        else: diff+=1; dd.append((t['e'].date(),str(t['x'].time())[:5],str(x.time())[:5] if x else None,t['reason'],why,round((xp-t['xp'])*t['qty']) if x else None))
    print(f'  {n[7:]:16} same-exit {same}  differ {diff}  no-local-data {miss} (engine pnl of those {missp:,.0f})')
    for d in dd: print('     ',d)
# 5 entry price vs option bar
t=T['renko6_tf5_x5_ema15tf'][0]
for ts,o,h,l,c in R.obars(t['sym']):
    if t['e']-timedelta(minutes=2)<=ts<=t['e']+timedelta(minutes=1): print('  bar',ts.time(),o,h,l,c,'| engine entry',t['ep'],'at',t['e'].time())
