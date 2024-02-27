global ch
def check(x,y,k,st) :
    if(k<=3) :
        if x%k<=int(k/3)+st and x%k>=k/3-st and y%k<=k/3+st and y%k>=k/3-st :
            global ch
            ch=1
    else :
        check(x, y, k/3)
i=0
n=int(input())
for i in range(1, n+1) :
    ch=0
    for j in range(1, n+1) :
        check(i, j, n)
        if ch==1:
            print(' ', end='')
        else:
            print('*', end='')
        ch=0
    print('\n')
    