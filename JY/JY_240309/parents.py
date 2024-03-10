import sys
from collections import deque
si=sys.stdin.readline
n=int(si().rstrip())
'graph=[[0]*(n+1) for i in range(n+1)]'
graph=[[] for i in range(n+1)]
visit=[0]*(n+1)
ans=[0]*(n+1)
'''
for i in range(n-1) :
    x, y = map(int, si().split())
    graph[x][y]=1
    graph[y][x]=1
'''

for i in range(n-1) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visit[1]=1
q=deque()
q.append(1)
while q : 
    x=q.popleft()
    for i in graph[x] :
        if  visit[i]==0 :
            visit[i]=1
            q.append(i)
            ans[i]=x
for i in range(2, n+1) :
    print(ans[i])