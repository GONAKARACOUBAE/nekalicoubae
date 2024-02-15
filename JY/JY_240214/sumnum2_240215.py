import sys
n, m = map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
low=high=0
hap=a[low]
ans=0
while True :
    if low == n :
        break
    if low>high :
        high=low
        hap=a[low]
    if hap == m :
        ans+=1
        high+=1
        if high!=n :
            hap+=a[high]
        else :
            hap-=a[low]
            low+=1
            if hap < m :
                break
    elif hap>m :
        hap-=a[low]
        low+=1
    else :
        high+=1
        if high!=n :
            hap+=a[high]
        else :
            hap-=a[low]
            low+=1
            if hap < m :
                break
print(ans)