import sys
from collections import defaultdict
n = int(sys.stdin.readline())
arr=defaultdict(int)
for i in range(n) :
    arr[sys.stdin.readline().split(".")]+=1
ans=sorted(arr, key = lambda x : x[0])
print(ans)
