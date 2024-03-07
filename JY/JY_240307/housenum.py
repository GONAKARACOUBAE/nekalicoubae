import sys
from collections import deque
n=int(sys.stdin.readline())
graph =[]
ch=[[0] * n for i in range(n)]
ans=0
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
num=[]
for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
for i in range(n) :
    for j in range(n) :
        if graph[i][j]==1 and ch[i][j]==0 :
            ch[i][j]=1
            ans+=1
            q=deque()
            q.append([i,j])
            cnt=1
            while q:
                x, y=q.popleft()
                for k in range(4) :
                    nowx=x+dx[k]
                    nowy=y+dy[k]
                    if nowx>=0 and nowx <n and nowy>=0 and nowy<n :
                        if graph[nowx][nowy] == 1 and ch[nowx][nowy] == 0 :
                            q.append([nowx, nowy])
                            ch[nowx][nowy]=1
                            cnt+=1
            num.append(cnt)
print(ans)
for i in num :
    print(i)
