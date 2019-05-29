st='Arad'
print(st)
ds='Bucharest'
qu=list()
cq=list()
nq=list()
count=dict()
cost=0
while(st != ds):
    f1 = open('graph.txt')
    f2 = open('finalgoal.txt')
    for line in f2:
        line=line.rstrip()
        words=line.split(' ')
        count[words[0]]=int(words[1])
    for line in f1:
        line=line.rstrip()
        words=line.split(' ')
        if st==words[0]:
            qu.append(words[1])
    print(qu)
    for a in qu:
        nq.append((count[a],a))
    nq=list(dict.fromkeys(nq))
    nq.sort()
    print(nq)
    st=nq[0][1]
    cost=cost+nq[0][0]
    nq.remove(nq[0])
    qu.remove(nq[0][1])
    print(st,'expend')
    print(nq)
print(cost)