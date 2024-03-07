import sys
n, c = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
arr.sort()
low=1
high=arr[-1]-arr[0]
ans=0
while low<=high :
    mid=(low+high)//2
    cur=arr[0]
    cnt=1
    for i in range(1, n) :
        if arr[i]-cur >= mid :
            cur=arr[i]
            cnt+=1
    if cnt>=c :
        if ans < mid :
            ans=mid
        low=mid+1
    else :
        high=mid-1
print(ans)
