goal=[0,1,2,3,4,5,6,7,8]
start=[3,1,2,0,4,5,6,7,8]
a=start
print(a)
qu=list()
qu.append(a)
print(qu)
c=0
count=0
while True:
    def check():
        if qu[count]==goal:
            print('Match')
            exit()
    def up(c):
        tem = qu[count][c]
        qu[count][c]=qu[count][c-3]
        qu[count][c-3]=tem
        print(qu[count])
        count=count+1
    def down(c):
        tem = qu[count][c]
        qu[count][c] = qu[count][c + 3]
        qu[count][c + 3] = tem
        print(qu[count])
        count = count + 1
    for i in range(9):
        if qu[count][i]==0:
            c=i
            print(c)
    if (c>=3 and c<=5):
        up(c)
        check()
        down(c)
        check()
        if c==3:
            right()
    elif c>=6 and c<=8:
        up(c)
        check()
    elif c>=0 and c<=2:
        down(c)
        check()
    count=count+1