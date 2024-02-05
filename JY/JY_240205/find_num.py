import sys
n=int(sys.stdin.readline())
arr_a=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr_b=list(map(int, sys.stdin.readline().split()))
for i in arr_b :
    print(i in arr_a)
