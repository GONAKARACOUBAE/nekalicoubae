import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph=[]
ch=[[0] * m for i in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
ans=sys.maxsize
for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
ch[0][0]=1
q=deque()
q.append([0, 0, 1])
while q :
    x, y, cnt=q.popleft()
    if x==n-1 and y == m-1 :
        print(cnt)
        break
    for i in range(4) :
        nowx=x+dx[i]
        nowy=y+dy[i]
        if nowx>= 0 and nowx<n and nowy>=0 and nowy<m :
            if ch[nowx][nowy]==0 and graph[nowx][nowy]==1 :
                ch[nowx][nowy]=1
                q.append([nowx, nowy, cnt+1])
    