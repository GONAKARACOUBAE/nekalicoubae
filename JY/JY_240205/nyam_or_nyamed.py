import sys
def bin(start, end, target, last=-1) :
    if start <= end:
        mid = (start + end)//2
        if arr_a[mid]==target :
            return mid
        elif arr_a[mid]>target :
            return bin(start, mid-1, target, last)
        else :
            return bin(mid+1, end, target, last)
    else :
        return start
t=int(sys.stdin.readline())
dap=[]
for i in range(t) :
    n, m=map(int,sys.stdin.readline().split())
    arr_a=list(map(int, sys.stdin.readline().split()))
    arr_b=list(map(int, sys.stdin.readline().split()))
    arr_a.sort()
    ans=0
    for j in arr_b :
        ans+=(n-bin(0, n-1, j)-1)
    dap.append(ans)
for i in dap :
    print(i)
