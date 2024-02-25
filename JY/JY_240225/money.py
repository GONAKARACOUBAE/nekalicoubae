import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
low=min(arr)
high=max(arr)
while True :
    mid=(low+high)//2
    hap=0
    for i in arr :
        if i < mid :
            hap+=i
        else :
            hap+=mid
    if hap>=m :
        ans=hap
        high=mid-1
    else :
        low=mid+1
    if low > high :
        break
print(ans)
