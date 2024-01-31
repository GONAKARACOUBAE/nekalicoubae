import sys
from collections import defaultdict
n = int(sys.stdin.readline())
arr=defaultdict(int)
for i in range(n) :
    arr[sys.stdin.readline().split(".")[1].rstrip()]+=1
ans=sorted(arr.items(), key = lambda x : x[0])
for i in ans :
    print("%s %d" % (i[0], i[1]))
