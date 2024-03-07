import sys
from collections import deque
def dfs(x, y, cnt) :
    if x==n-1 and y==m-1 :
        global ans
        if cnt < ans :
            ans=cnt
    for i in range(4) :
        nowx=x+dx[i]
        nowy=y+dy[i]
        if nowx>=0 and nowy>=0 and nowx<n and nowy<m :
            if graph[nowx][nowy]==1 and ch[nowx][nowy]==0 :
                ch[nowx][nowy]=1
                dfs(nowx, nowy, cnt+1)
                ch[nowx][nowy]=0
n, m = map(int, sys.stdin.readline().split())
graph=[]
ch=[[0] * m for i in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
ans=sys.maxsize
for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
ch[0][0]=1
dfs(0, 0, 1)
print(ans)