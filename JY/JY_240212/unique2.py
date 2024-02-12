import sys
n = int(sys.stdin.readline())
arr= list(map(int, sys.stdin.readline().split()))
low=high=0
cnt=[0]*100001
ans=0
while True :
    if low==n:
        break
    if high == n :
        high-=1
        ans+=(high-low)+1
        cnt[arr[low]]=0
        low+=1
    elif cnt[arr[high]]==1 :
        high-=1
        ans+=(high-low)+1
        cnt[arr[low]]=0
        low+=1
    else :
        cnt[arr[high]]=1
    high+=1
print(ans)