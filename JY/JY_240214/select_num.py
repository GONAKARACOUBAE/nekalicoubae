import sys
n, m = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
low=0
high=1
ans=sys.maxsize
while True :
    if  high==n :
        break
    temp=arr[high]-arr[low]
    if temp >= m and ans>temp :
        ans=temp
        if temp==m :
            break
    if temp > m :
        low+=1
        high=low+1
    else :
        high+=1

print(ans)
    