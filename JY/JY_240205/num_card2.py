import sys
from collections import defaultdict
nrr=defaultdict(int)
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
for i in a :
    nrr[i]+=1
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))
for j in b :
    print(nrr[j], end=" ")