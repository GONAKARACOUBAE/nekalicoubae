import sys
def binary(start, end, target) :
    mid=int((start+end)/2)
    if arr_a[mid]==target :
        return 1
    if start>end :
        return 0
    if arr_a[mid]>target :
        return binary(start, mid-1, target)
    else :
        return binary(mid+1, end, target)
n=int(sys.stdin.readline())
arr_a=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr_b=list(map(int, sys.stdin.readline().split()))
arr_a.sort()
for i in arr_b :
    print(binary(0, n-1, i))