import sys
from collections import deque
si=sys.stdin.readline
r, c = map(int, si().split())
graph=[]
ch=[[0] * c for i in range(r)]
sheep=deque()
q=deque()
wcnt=0
scnt=0
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
for i in range(r) :
    graph.append(list(map(str, si().rstrip())))
for i in range(r) :
    for j in range(c) :
        if graph[i][j] == 'o' :
            sheep.append([i, j])
            scnt+=1
        elif graph[i][j] == 'v' :
            wcnt+=1
while sheep :
    q.append(sheep.popleft())
    scnt_now=1
    wcnt_now=0
    while q :
        x, y = q.popleft()
        ch[x][y]=1
        for i in range(4) :
            nowx=x+dx[i]
            nowy=y+dy[i]
            if 0<=nowx<r and 0<=nowy<c :
                if ch[nowx][nowy]==0  and graph[nowx][nowy]!='#':
                    q.append([nowx, nowy])
                    ch[nowx][nowy]=1
                    if graph[nowx][nowy]=='o' :
                        scnt_now+=1
                        sheep.remove([nowx, nowy])
                    elif graph[nowx][nowy]=='v' :
                        wcnt_now+=1
    if wcnt_now>=scnt_now :
        scnt-=scnt_now
    else :
        wcnt-=wcnt_now
print(scnt, wcnt)
                        
            