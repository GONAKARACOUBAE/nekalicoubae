import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
arr=[]
x=y=0
while True :
    if y==m :
        for i in range(x, n) :
            arr.append(a[i])
        break
    elif x==n :
        for i in range(y, m) :
            arr.append(b[i])
        break
    if a[x]<b[y] :
        arr.append(a[x])
        x+=1
    else :
        arr.append(b[y])
        y+=1
for i in range(n+m) :
    print(arr[i], end=' ')