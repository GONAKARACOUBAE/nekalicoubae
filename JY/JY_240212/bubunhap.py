import sys
n, s = map(int, sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
low=high=0
hap=arr[0]
ans=sys.maxsize
ch=0
while True :
    if hap == 0 :
        break
    if hap<s :
        high+=1
        if high==n :
            break
        hap+=arr[high]
    else :
        ch=1
        if ans>high-low+1 :
            ans=high-low+1
        hap-=arr[low]
        low+=1
if ch == 0 :
    print(0)
else :
    print(ans)