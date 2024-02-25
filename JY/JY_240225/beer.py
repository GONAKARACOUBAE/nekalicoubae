import sys
n, k = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
low=1
high=max(arr)
ans=0
while True :
    mid=(low+high)//2
    cnt=0
    ch=0
    for i in arr :
        cnt+=i//mid
    if cnt>=k :
        ans = mid
        low=mid+1
    else :
        high=mid-1
    if low > high :
        break
print(ans)
            
