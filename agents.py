a=10
b=5
fhand=open('agent.txt')
for line in fhand:
    line=line.rstrip()
    words=line.split(' ')
    for word in words:
        if(word=='add'):
            print('add a,b:',a+b)
        elif (word == 'subtract'):
            print('subtract b from a:',a - b)
        elif(word=='multiple'):
            print('multiple a,b:',a*b)
        elif(word=='divide'):
            print('divide a by b:',a/b)
        else:
            print('Do Nothing')