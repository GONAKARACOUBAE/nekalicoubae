import sys
from collections import defaultdict
n=int(input())
arr = defaultdict(list)
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)
ans = 0


for i in arr.keys() :
    arr[i].sort()
    for j in range(len(arr[i])) :
        if j == 0 :
            ans+=arr[i][1]-arr[i][0]
        elif j==len(arr[i])-1 :
            ans+=arr[i][len(arr[i])-1]-arr[i][len(arr[i])-2]
        else :
            if arr[i][j]-arr[i][j-1] > arr[i][j+1]-arr[i][j] :
                ans+=arr[i][j+1]-arr[i][j]
            else :
                ans+=arr[i][j]-arr[i][j-1]
print(ans)