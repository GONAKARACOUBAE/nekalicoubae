import sys
n = int(sys.stdin.readline())
arr= list(map(int, sys.stdin.readline().split()))
x=int(sys.stdin.readline())
arr.sort()
low=0
high=n-1
ans=0
while True :
    if low>=high :
        break
    hap=arr[low]+arr[high]
    if hap == x :
        ans+=1
        high-=1
        low+=1
    elif hap > x :
        high-=1
    else :
        low+=1
print(ans)
