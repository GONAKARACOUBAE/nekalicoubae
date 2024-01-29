import sys
from collections import defaultdict
n=int(input())
arr = defaultdict(int)
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    if (b in arr) == False :
        arr[b]=a
    else :
        arr[b].append(a)
print(arr)