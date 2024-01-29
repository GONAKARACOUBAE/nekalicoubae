import sys
from collections import defaultdict
n=int(input())
arr = defaultdict(list)
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)
print(arr)