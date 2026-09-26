import json, collections
import replay as R, bricks as BR
P={}
for f in ('../../sweep_configs/renko5_overnight_batch.txt','../../sweep_configs/renko6_candle_exit5_batch.txt','../../sweep_configs/renko7_entry_batch.txt'):
    for line in open(f):
        if line.startswith('#') or not line.strip(): continue
        n,_,p=line.strip().split('|',2); P[n]=json.loads(p)
CFG={'BASE ema15tf':('renko6','renko6_tf5_x5_ema15tf'),'E4 b10':('renko7','renko7_e4_tf5_b1000'),'TF5X5':('renko6','renko6_tf5_x5'),
     'MV50 b625ext':('renko5','renko5_b625_mv50ext'),'B833MV50':('renko5','renko5_b833_mv50')}
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def mdd(p):
    c=pk=d=0
    for a in p: c+=a; pk=max(pk,c); d=max(d,pk-c)
    return d
V=[('cexit5',dict(rev_early=30,rev_late=30,cexit=5)),('cexit6',dict(rev_early=30,rev_late=30,cexit=6)),('cexit7',dict(rev_early=30,rev_late=30,cexit=7)),('cexit8',dict(rev_early=30,rev_late=30,cexit=8)),
   ('rev1',dict()),('rev2',dict(rev_early=2,rev_late=2)),('cexit6+rev1',dict(cexit=6)),('cexit7+rev1',dict(cexit=7)),('cexit8+rev1',dict(cexit=8)),
   ('cexit5+BE2',dict(rev_early=30,rev_late=30,cexit=5,be_at=2)),('cexit5+BE3',dict(rev_early=30,rev_late=30,cexit=5,be_at=3)),('cexit5+BE4',dict(rev_early=30,rev_late=30,cexit=5,be_at=4)),
   ('cexit7+BE3',dict(rev_early=30,rev_late=30,cexit=7,be_at=3)),('rev1+BE3',dict(be_at=3)),('cexit7+rev1+BE3',dict(cexit=7,be_at=3)),
   ('cexit5+noprog4',dict(rev_early=30,rev_late=30,cexit=5,noprog=4))]
QC=[]
for name,(d,cn) in CFG.items():
    p=P[cn]; B=p['fixed_brick_size_points']; tf=p['brick_source_timeframe_minutes']
    allT=sorted(R.load_trades(f'{d}/{cn}_current.csv'),key=lambda t:t['e'])
    T=[t for t in allT if t['sym'] in R.idx and t['e'].date() in R.Ub]
    eng_kw=dict(rev_early=30,rev_late=30,cexit=p['candle_exit_confirm']) if p.get('candle_exit_confirm') else {}
    # parity vs engine
    same=diff=0; dd=[]
    for t in T:
        x,xp,why=BR.sim(t,B,tf,**eng_kw)
        if x==t['x'] and abs(xp-t['xp'])<0.01: same+=1
        else: diff+=1; dd.append((t['e'].date(),t['reason'],why,round((xp-t['xp'])*t['qty']) if x else None))
    miss=[t for t in allT if t not in T]
    byday=collections.defaultdict(list)
    for t in allT: byday[t['e'].date()].append(t)
    print(f"\n=== {name} B={B} tf={tf} | replay {len(T)}/{len(allT)} | uncovered engine pnl {sum(t['pnl'] for t in miss):,.0f} | parity same {same} diff {diff} {dd if dd else ''}")
    print(f" {'variant':16} n  net  PF WR% avgW avgL DD ex2 CE PE H1 H2 | same-day-conflicts")
    for lab,kw in V:
        rows=[]
        for t in T:
            x,xp,why=BR.sim(t,B,tf,**kw)
            if x is None: continue
            rows.append((t,(xp-t['ep'])*t['qty'],x))
        pp=[a for _,a,_ in rows]; h=len(pp)//2; w=[a for a in pp if a>0]; l=[a for a in pp if a<0]
        conf=0
        for t,a,x in rows:
            nxt=[u for u in byday[t['e'].date()] if u['e']>t['e']]
            if nxt and x>min(u['e'] for u in nxt): conf+=1
        print(f" {lab:16} {len(pp)} {sum(pp):>7,.0f} {pf(pp):4.2f} {100*len(w)/len(pp):2.0f} {sum(w)/len(w):>5,.0f} {sum(l)/len(l):>6,.0f} {mdd(pp):>6,.0f} {sum(sorted(pp)[:-2]):>7,.0f} "
              f"{sum(a for t,a,_ in rows if t['ce']):>6,.0f} {sum(a for t,a,_ in rows if not t['ce']):>6,.0f} {sum(pp[:h]):>6,.0f} {sum(pp[h:]):>6,.0f} | {conf}")
