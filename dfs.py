queue = list()
snode = 'aa'
print(snode)
gnode = 'hh'
while snode != gnode :
    fh = open('bfsDfs.txt')
    for line in fh:
        line=line.rstrip()
        words=line.split(' ')
        if snode==words[0]:
            queue.append(words[1])
    print(queue)
    if gnode in queue:
       break
    le=len(queue)
    snode=queue[le-1]
    print(snode)
    queue.remove(snode)