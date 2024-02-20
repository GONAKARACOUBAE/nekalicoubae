import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
l=list(range(1,n+1))
for i in permutations(l, m) :
    for j in range(m) :
        print(i[j], end=" ")
    print()
