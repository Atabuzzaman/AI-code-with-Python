st='Arad'
print(st)
ds='Bucharest'
qu=list()
nq=list()
count=dict()
count2=dict()
q=dict()
q['Arad']=0
while( st != ds ):
    f1 = open('graph.txt')
    f2 = open('finalgoal.txt')
    for line1 in f2:
        line1=line1.rstrip()
        words=line1.split(' ')
        count[words[0]]=int(words[1])

    for line in f1:
        line=line.rstrip()
        words=line.split(' ')
        if st==words[0]:
            qu.append(words[1])
            count2[words[1]] = int(words[2])+q[st]
    for a in qu :
        nq.append((count[a]+count2[a],a))
    nq=list(dict.fromkeys(nq))
    nq.sort()
    print(nq)
    st=nq[0][1]
    nq.remove(nq[0])
    qu.remove(st)
    print(qu)
    q[st]=count2[st]
    print(st,'expend')
    print(nq)