import sys
from itertools import combinations
n, s = map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))
ans=0
per=[]
idx=[]
for i in range(1, len(arr)+1) :
    idx.append(i)
for i in range(1, len(arr)+1) :
    per+=list(combinations(idx, i))
for i in per :
    hap=0
    for j in i :
        hap+=arr[j-1]
    if hap == s :
        ans+=1
print(ans)