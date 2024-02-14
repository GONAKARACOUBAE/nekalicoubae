import sys
n, m = map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
low=high=0
hap=a[low]
ans=0
while True :
    if low>high :
        break
    if hap <= m :
        if high+1<=n :
            high+=1
            hap+=a[high]
        else :
            break
    else :
        hap-=a[low]
        low+=1
    if hap == m :
        ans+=1
print(ans)