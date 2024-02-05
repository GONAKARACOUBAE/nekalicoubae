import sys
n=int(sys.stdin.readline())
arr_a=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr_b=list(map(int, sys.stdin.readline().split()))
arr_a.sort()
for i in arr_b :
    left=0
    right=n-1
    while left<right :
        idx=int((left+right+1)/2)
        if arr_a[idx] < i :
            left=idx+1
        else :
            right=idx-1
    if arr_a[left]==i :
        print(1)
    else :
        print(0)
    