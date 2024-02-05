import sys
t=int(sys.stdin.readline())
dap=[]
for i in range(t) :
    n, m=map(int,sys.stdin.readline().split())
    arr_a=list(map(int, sys.stdin.readline().split()))
    arr_b=list(map(int, sys.stdin.readline().split()))
    arr_a.sort()
    arr_b.sort()
    ans=0
    for j in arr_b :
        left=0
        right=n-1
        while left!=right :
            idx = int((left + right + 1) /2)
            if arr_a[idx] <= j :
                left=idx
            elif arr_a[idx] >= j :
                right=idx-1
        ans+=n-left-1
    dap.append(ans)
for i in dap :
    print(i)