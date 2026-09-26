import replay as R, sys
from collections import Counter
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else float('inf')
def run(T,B,tf,label,**kw):
    res=[]
    for t in T:
        r=R.simulate(t,B,tf,**kw)
        if r is None or 'err' in r or r['x'] is None: continue
        res.append((t,r,R.pnl(t,r)))
    p=[x[2] for x in res]; n=len(p)
    s=sorted(p,reverse=True); ex=p[:]; 
    for v in s[:2]: ex.remove(v)
    half=n//2; ce=[x[2] for x in res if x[0]['ce']]; pe=[x[2] for x in res if not x[0]['ce']]
    ordr=sorted(res,key=lambda x:x[0]['e']); h1=[x[2] for x in ordr[:half]]; h2=[x[2] for x in ordr[half:]]
    hold=sorted((x[1]['x']-x[0]['e']).total_seconds()/60 for x in res)
    ex_mix=Counter(x[1]['reason'] for x in res)
    print(f"{label:34} n={n} net={sum(p):>8,.0f} PF={pf(p):4.2f} WR={100*sum(v>0 for v in p)/n:3.0f}% exTop2={sum(ex):>7,.0f}/{pf(ex):4.2f} | CE {sum(ce):>7,.0f}/{pf(ce):4.2f} PE {sum(pe):>7,.0f}/{pf(pe):4.2f} | H1 {sum(h1):>6,.0f} H2 {sum(h2):>6,.0f} | medHold {hold[n//2]:.0f}m {dict(ex_mix)}")
    return res
if __name__=='__main__':
    path,B,tf=sys.argv[1],float(sys.argv[2]),int(sys.argv[3])
    T=R.load_trades(path)
    run(T,B,tf,'static n=1 (baseline, validated)',struct=('static',1))
    run(T,B,tf,'static n=3 (2a control)',struct=('static',3))
    run(T,B,tf,'no structure exit',struct=None)
    run(T,B,tf,'dyn n=1 +trail+tgt',struct=('dyn',1))
    run(T,B,tf,'dyn n=2 +trail+tgt',struct=('dyn',2))
    run(T,B,tf,'dyn n=3 +trail+tgt',struct=('dyn',3))
    run(T,B,tf,'dyn n=1 stop only (no trail/tgt)',struct=('dyn',1),trail=None,target_pct=None)
    run(T,B,tf,'dyn n=2 stop only',struct=('dyn',2),trail=None,target_pct=None)
    run(T,B,tf,'dyn n=3 stop only',struct=('dyn',3),trail=None,target_pct=None)
    run(T,B,tf,'stop only, no struct/trail/tgt',struct=None,trail=None,target_pct=None)
