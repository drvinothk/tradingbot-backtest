import json, re, statistics as st, collections
from datetime import date
import replay as R, bricks as BR
DN=['Mon','Tue','Wed','Thu','Fri']
def dte(t):
    m=re.search(r'NIFTY(\d{2})(\d{2})(\d{2})',t['sym']); return (date(2000+int(m[1]),int(m[2]),int(m[3]))-t['e'].date()).days
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def mdd(p):
    c=pk=d=0
    for a in p: c+=a; pk=max(pk,c); d=max(d,pk-c)
    return d
def line(lab,p):
    if not p: return f"{lab:28} n=0"
    h=len(p)//2
    return f"{lab:28} n={len(p):3} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):2.0f}% avg={st.mean(p):>6,.0f} DD={mdd(p):>6,.0f} ex2={sum(sorted(p)[:-2]) if len(p)>2 else 0:>7,.0f} H1={sum(p[:h]):>6,.0f} H2={sum(p[h:]):>6,.0f}"
CF={'BASE':('perday1/pd1_base_current.csv','renko6','renko6_tf5_x5_ema15tf'),'MV50':('perday1/pd2_mv50_current.csv','renko5','renko5_b625_mv50ext')}
P={}
for f in ('../../sweep_configs/renko5_overnight_batch.txt','../../sweep_configs/renko6_candle_exit5_batch.txt'):
    for l in open(f):
        if l.startswith('#') or not l.strip(): continue
        n,_,q=l.strip().split('|',2); P[n]=json.loads(q)
T={k:sorted(R.load_trades(v[0]),key=lambda t:t['e']) for k,v in CF.items()}
def sim_stop(t,B,tf,stop_pct=0.35,**kw):
    """bricks.sim + the engine's intrabar premium stop (bar low <= rt(entry*(1-stop_pct)), exit at the stop price). The engine checks the
    stop before the other exits within a bar, so if the stop bar is <= the variant's exit bar the stop wins."""
    x,xp,why=BR.sim(t,B,tf,**kw)
    stop=R.rt(t['ep']*(1-stop_pct))
    for ts,o,h,l,c in R.obars(t['sym']):
        if ts<t['e']: continue
        if x is not None and ts>x: break
        if l<=stop: return ts,stop,'stop'
    return x,xp,why
print("=== 1. by days-to-expiry x side (per-day, one trade/day)")
for k,ts in T.items():
    print(k)
    for d in (0,1,4,5,6):
        for side,fl in (('both',None),('CE',True),('PE',False)):
            p=[t['pnl'] for t in ts if dte(t)==d and (fl is None or t['ce']==fl)]
            if side=='both': print('  DTE',d,line('',p))
            else: print('        ',line(side,p))
print("\n=== 2. DTE gates (in-sample; then chosen-on-H1 -> tested-on-H2)")
gates={'all':lambda t:True,'no Tue':lambda t:dte(t)!=0,'DTE>=4':lambda t:dte(t)>=4,'DTE>=5':lambda t:dte(t)>=5,'DTE6 only':lambda t:dte(t)==6,'no Tue,no Thu':lambda t:dte(t) not in (0,5)}
for k,ts in T.items():
    print(k); h=len(ts)//2
    for g,fn in gates.items():
        p=[t['pnl'] for t in ts if fn(t)]; a=[t['pnl'] for t in ts[:h] if fn(t)]; b=[t['pnl'] for t in ts[h:] if fn(t)]
        print('  ',line(g,p),f"| H1-sel {sum(a):>7,.0f}  H2-test {sum(b):>7,.0f}")
print("\n=== 3. exit variants on the per-day entries (replay; entries fixed), all days vs DTE6 vs non-DTE6")
V=[('engine-equivalent',None),('cexit5',dict(rev_early=30,rev_late=30,cexit=5)),('cexit6',dict(rev_early=30,rev_late=30,cexit=6)),('cexit7',dict(rev_early=30,rev_late=30,cexit=7)),('cexit8',dict(rev_early=30,rev_late=30,cexit=8)),
   ('rev1',dict()),('rev2',dict(rev_early=2,rev_late=2)),('cexit7+rev1',dict(cexit=7)),('cexit5+BE3',dict(rev_early=30,rev_late=30,cexit=5,be_at=3)),('rev1+BE3',dict(be_at=3)),('cexit5+noprog4',dict(rev_early=30,rev_late=30,cexit=5,noprog=4))]
for k,(f,d,cn) in CF.items():
    p=P[cn]; B=p['fixed_brick_size_points']; tf=p['brick_source_timeframe_minutes']
    eng=dict(rev_early=30,rev_late=30,cexit=p['candle_exit_confirm']) if p.get('candle_exit_confirm') else {}
    ts=[t for t in T[k] if t['sym'] in R.idx and t['e'].date() in R.Ub]
    print(f"{k}: replay covers {len(ts)}/{len(T[k])} trades")
    same=sum(1 for t in ts if (lambda r:(r[0]==t['x'] and abs(r[1]-t['xp'])<0.01))(sim_stop(t,B,tf,**eng)))
    print(f"  engine-equivalent parity: {same}/{len(ts)} identical exits")
    for lab,kw in V:
        rows=[]
        for t in ts:
            x,xp,why=sim_stop(t,B,tf,**(eng if kw is None else kw))
            if x is not None: rows.append((t,(xp-t['ep'])*t['qty']))
        a=[v for _,v in rows]; w6=[v for t,v in rows if dte(t)==6]; o=[v for t,v in rows if dte(t)!=6]
        print(f"  {lab:18} all n={len(a)} net={sum(a):>7,.0f} PF={pf(a):4.2f} DD={mdd(a):>6,.0f} | DTE6 net={sum(w6):>7,.0f} PF={pf(w6):4.2f} | other net={sum(o):>7,.0f} PF={pf(o):4.2f}")
print("\n=== 4. day-wise strategy idea: weekday x config, and pick-by-H1 -> test-on-H2")
def dayset(ts): 
    d=collections.defaultdict(list)
    for t in ts: d[t['e'].weekday()].append(t)
    return d
D={k:dayset(ts) for k,ts in T.items()}
print('weekday   '+'  '.join(f"{k}(n,net,PF)" for k in T))
for wd in range(5):
    print(f"{DN[wd]:8}  "+'  '.join(f"({len(D[k][wd])},{sum(t['pnl'] for t in D[k][wd]):>7,.0f},{pf([t['pnl'] for t in D[k][wd]]):.2f})" for k in T))
# split by calendar half (first half of period vs second half)
alld=sorted({t['e'].date() for ts in T.values() for t in ts}); cut=alld[len(alld)//2]
print('calendar split at',cut)
comb1=comb2=0; 
for wd in range(5):
    h1={k:sum(t['pnl'] for t in D[k][wd] if t['e'].date()<cut) for k in T}; h2={k:sum(t['pnl'] for t in D[k][wd] if t['e'].date()>=cut) for k in T}
    best=max(h1,key=h1.get); pick=best if h1[best]>0 else 'none'
    print(f"  {DN[wd]}: H1 {({k:round(v) for k,v in h1.items()})} -> pick {pick}; H2 {({k:round(v) for k,v in h2.items()})} -> H2 result {round(h2.get(pick,0)) if pick!='none' else 0}")
    comb2+= h2.get(pick,0) if pick!='none' else 0
print('  day-wise pick (chosen on H1) result on H2:',round(comb2),' vs H2 of BASE all days',round(sum(t['pnl'] for t in T['BASE'] if t['e'].date()>=cut)),' MV50 all days',round(sum(t['pnl'] for t in T['MV50'] if t['e'].date()>=cut)))
print("\n=== 5. overlap: same day, both configs trade?")
bd={t['e'].date():t for t in T['BASE']}; md={t['e'].date():t for t in T['MV50']}
both=set(bd)&set(md); print('days both traded',len(both),'base only',len(set(bd)-set(md)),'mv50 only',len(set(md)-set(bd)),'same direction',sum(1 for d in both if bd[d]['ce']==md[d]['ce']))
