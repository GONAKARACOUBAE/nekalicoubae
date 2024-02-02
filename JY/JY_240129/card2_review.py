import sys
from collections import defaultdict
n=int(sys.stdin.readline())
a=defaultdict(int)
for i in range(n) :
    num=int(sys.stdin.readline().rstrip())
    a[num]+=1
ans=sorted(a.items(), key = lambda item : (-item[1], item[0]))
print(ans[0][0])