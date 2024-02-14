import sys
n, m = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
low=0
high=len(arr)-1
ans=sys.maxsize
while True :
    temp=arr[high]-arr[low]
    if low >= high or temp < m :
        break
    if temp >= m and temp < ans :
        ans=temp
    if arr[high]-arr[low+1] < arr[high-1]-arr[low] :
        low+=1
    else :
        high-=1
print(ans)
    