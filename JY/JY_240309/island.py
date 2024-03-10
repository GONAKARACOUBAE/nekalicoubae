import sys
from collections import deque
si=sys.stdin.readline
dx=[1, -1, 0, 0, 1, 1, -1, -1]
dy=[0, 0, 1, -1, 1, -1, 1, -1]
ans=[]
while True :
    w, h = map(int, si().split())
    if w==0 and h ==0 :
        break
    graph=[]
    q=deque()
    ch=[[0]*w for i in range(h)]
    cnt=0
    for i in range(h) :
        graph.append(list(map(int, si().split())))
    for i in range(h) :
        for j in range(w) :
            if graph[i][j]==1 and ch[i][j]==0 :
                ch[i][j]=1
                q.append([i, j])
                cnt+=1
                while q :
                    x, y = q.popleft()
                    for k in range(8) :
                        nowx=x+dx[k]
                        nowy=y+dy[k]
                        if 0<=nowx < h and 0<=nowy < w :
                            if graph[nowx][nowy]==1 and ch[nowx][nowy]==0 :
                                q.append([nowx, nowy])
                                ch[nowx][nowy]=1
    ans.append(cnt)
for i in ans :
    print(i)                
