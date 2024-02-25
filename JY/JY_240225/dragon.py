import sys
n, m = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
low=min(arr)
high=sum(arr)
ans=0
while low<=high :
    mid=(low+high)//2
    money=mid
    cnt=1
    for i in arr :
        if money-i < 0 :
            cnt+=1
            money=mid
            money-=i
        else :
            money-=i
    if cnt > m or mid < max(arr) :
        low=mid+1 
    else :
        high=mid-1
        ans=mid
print(ans)