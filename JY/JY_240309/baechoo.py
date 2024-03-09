import sys
from collections import deque
t=int(sys.stdin.readline().rstrip())
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
ans=[]
for i in range(t) :
    m, n, k = map(int, sys.stdin.readline().split())
    graph=[[0]*m for e in range(n)]
    ch=[[0]*m for e in range(n)]
    q=deque()
    cnt=0
    for j in range(k) :
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y]=1
    for l in range(n) :
        for j in range(m) :
            if ch[l][j]==0 and graph[l][j]==1 :
                q.append([l, j])
                ch[l][j]=1
                cnt+=1
                while q :
                    xx, yy = q.popleft()
                    for d in range(4) :
                        nowx=xx+dy[d]
                        nowy=yy+dx[d]
                        if 0<= nowx < n and 0<= nowy <m :
                            if ch[nowx][nowy]==0 and graph[nowx][nowy]==1 :
                                ch[nowx][nowy]=1
                                q.append([nowx, nowy])
    ans.append(cnt)
for i in ans :
    print(i)
