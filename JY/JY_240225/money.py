import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
low=0
high=max(arr)
ans=0
while True :
    mid=(low+high)//2
    hap=0
    for i in arr :
        if i < mid :
            hap+=i
        else :
            hap+=mid
    if hap>m :
        high=mid-1
    else :
        ans=mid
        low=mid+1
    if low > high :
        break
print(ans)
