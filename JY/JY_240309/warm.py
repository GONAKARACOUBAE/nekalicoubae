import sys
from collections import deque
si=sys.stdin.readline
n = int(si().rstrip())
m = int(si().rstrip())
graph=[[0]*(n+1) for i in range(n+1)]
visit=[0]*(n+1)
for i in range(m) :
    x, y = map(int, si().split())
    graph[x][y]=1
    graph[y][x]=1
q=deque()
q.append(1)
visit[1]=1
cnt=0
while q : 
    t=q.popleft()
    for i in range(1, n+1) :
        if graph[t][i] == 1 and visit[i]==0 :
            q.append(i)
            visit[i]=1
            cnt+=1
print(cnt)
