import sys
from collections import deque
si=sys.stdin.readline
n, m =map(int, si().split())
ch=[[0]*(n+1) for i in range(n+1)]
graph=[[0]*(n+1) for i in range(n+1)]
ans=0
q=deque()
for i in range(m) :
    x, y = map(int, si().split())
    graph[x][y]=1
    graph[y][x]=1
for i in range(1, n+1) :
    for j in range(i+1, n+1) :
        if graph[i][j]==1 and ch[i][j]==0 :
            ch[i][j]=1
            ch[j][i]=1
            ans+=1
            q.append(j)
            while q :
                y = q.popleft()
                for k in range(1, n+1) :
                    if graph[y][k]==1 and ch[y][k]==0 :
                        ch[y][k]=1
                        ch[k][y]=1
                        q.append(k)
print(ans)
                
