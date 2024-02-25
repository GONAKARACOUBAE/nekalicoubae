import sys
n, k = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
low=0
high=max(arr)
ans=0
while True :
    mid=(low+high)//2
    cnt=0
    ch=0
    for i in arr :
        while True :
            if i-mid<0:
                break
            else :
                i-=mid
                cnt+=1
    if cnt==k and ans<mid:
        ans=mid
        break
    if cnt>k :
        low=mid+1
    else :
        high=mid-1
    if low > high :
        break
print(ans)
            
