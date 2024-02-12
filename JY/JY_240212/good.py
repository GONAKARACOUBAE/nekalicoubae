import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
ans=0
for i in range(n) :
    low=0
    high=n-1
    while True :
        if low == i :
            low+=1
        if high == i :
            high -=1
        if low==high :
            break
        if a[low]+a[high] > a[i] :
            high-=1
        elif a[low]+a[high] < a[i] :
            low+=1
        else :
            ans+=1
            break
print(ans)