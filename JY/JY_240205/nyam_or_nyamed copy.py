import sys
from collections import defaultdict
t=int(sys.stdin.readline())
dap=[]
for i in range(t) :
    dic=defaultdict(int)
    ans=0
    n, m=map(int,sys.stdin.readline().split())
    arr_a=list(map(int, sys.stdin.readline().split()))
    for j in arr_a :
        dic[j]+=1
    arr_b=list(map(int, sys.stdin.readline().split()))
    for j in arr_b :
        for keys, values in dic.items() :
            if keys > j :
                ans+=values
    dap.append(ans)
for i in dap :
    print(i)
