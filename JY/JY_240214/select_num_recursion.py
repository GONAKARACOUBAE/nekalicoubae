import sys
sys.setrecursionlimit(10**9)
def search(low, high) :
    global ans
    global m
    temp=arr[high]-arr[low]
    if low > high or temp < m :
        return 0
    if temp >= m and temp < ans :
        ans=temp
    search(low+1, high)
    search(low,high-1)
n, m = map(int, sys.stdin.readline().split())
arr=[]
for i in range(n) :
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
low=0
high=len(arr)-1
ans=sys.maxsize
search(low, high)
print(ans)
    