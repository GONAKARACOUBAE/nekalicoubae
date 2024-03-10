import sys
from collections import deque
si=sys.stdin.readline
n = int(si().rstrip())
graph=[]
ans=[[0]*n for i in range(n)]
for i in range(n) :
    graph.append(list(map(int, si().split())))
for i in range(n) :
    for j in range(n) :
        if graph[i][j]==1 :
            ans[i][j]=1            
            q=deque()   
            q.append(j)
            while q :
                x=q.popleft()
                for k in range(n) :
                    if graph[x][k]==1 and ans[i][k]==0 :
                        q.append(k)
                        ans[i][k]=1
for i in range(n) :
    for j in range(n) :
        print(ans[i][j], end=" ")
    print()