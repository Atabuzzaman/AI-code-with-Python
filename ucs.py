st='Sibiu'
print(st)
ds='Bucharest'
qu=list()
nq=list()
count=dict()
q=dict()
q['Sibiu']=0
while( st != ds ):
    f1 = open('ucsgraph.txt')
    for line in f1:
        line=line.rstrip()
        words=line.split(' ')
        if st==words[0]:
            qu.append(words[1])
            count[words[1]] = int(words[2])+q[st]

    print(qu)
    for a in qu :
        nq.append((count[a],a))
    nq=list(dict.fromkeys(nq))
    nq.sort()
    print(nq)
    st=nq[0][1]
    nq.remove(nq[0])
    qu.remove(st)
    print(qu)
    q[st]=count[st]
    print(st,'expend')