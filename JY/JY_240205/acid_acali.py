import sys
sys.setrecursionlimit(10**6)
def search(low, high, min) :
    if low>=high :
        return 0
    if abs(arr[low]+arr[high]) < min :
        ans[0]=arr[low]
        ans[1]=arr[high]
        min=abs(arr[low]+arr[high])
    search(low+1, high, min)
    search(low, high-1, min)
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
arr.sort()
ans=[0, 0]
search(0, n-1, sys.maxsize)
print(ans[0], ans[1])
#시간초과.


