queue = list()
clq = list()
snode = 'aa'
print(snode)
clq.append(snode)
gnode = 'hh'
while snode != gnode:
    fh = open('bfsDfs.txt')
    for line in fh:
        line=line.rstrip()
        words=line.split(' ')
        if snode==words[0]:
            queue.append(words[1])
    print(queue)
    if gnode in queue:
        break
    clq.append(queue[0])
    snode = queue[0]
    print(snode)
    queue.remove(queue[0])
print('Expanded Node:',clq,gnode)