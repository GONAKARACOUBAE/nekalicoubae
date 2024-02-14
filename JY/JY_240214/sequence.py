import sys
n, k = map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))
ans=0
hap=0
high=k-1
for i in range(k) :
    hap+=arr[i]
ans=hap
while True :
    high+=1
    if high == n :
        break
    hap+=arr[high]
    hap-=arr[high-k]
    if hap > ans :
        ans=hap
print(ans)