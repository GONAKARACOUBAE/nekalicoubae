import sys
def sumarr(x, y, arr) :
    if y==m :
        for i in range(x, n) :
            arr.append(a[i])
        return arr
    elif x==n :
        for i in range(y, m) :
            arr.append(b[i])
        return arr
    if a[x]<b[y] :
        arr.append(a[x])
        return sumarr(x+1, y, arr)
    else :
        arr.append(b[y])
        return sumarr(x, y+1, arr)
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
ans=[]
print(sumarr(0,0, ans))