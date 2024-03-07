import sys
from collections import defaultdict
from collections import deque
def dfs(now) :
    chd[now]=1
    print(now, end=" ")
    for i in range(1, n+1) :
        if graph[now][i]==True and chd[i]==0 :
            dfs(i)
def bfs(now) :
    q = deque([now])
    chb[now]=1
    while q : 
        x=q.popleft()
        print(x, end=" ")
        for i in range(1, n+1) :
            if graph[x][i]==True and chb[i]==0 :
                q.append(i)
                chb[i]=1

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n+1) for i in range(n+1)]
chd=[0]*(n+1)
chb=[0]*(n+1)
d=[]
b=[]
for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b]=True
    graph[b][a]=True
dfs(v)
print()
bfs(v)
