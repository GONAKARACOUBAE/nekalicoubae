import sys
from collections import defaultdict
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ch=defaultdict(int)
for i in combinations(arr, m) :
    print(type(i))