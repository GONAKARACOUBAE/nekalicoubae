import sys        
from collections import deque
a, b, c = map(int, sys.stdin.readline().split())
ch=[[[0 for col in range(201)] for row in range(201)] for depth in range(201)]
ans=[]
ans.append(c)
q=deque()
q.append([a, b, c])
while q :
    x, y, z = q.popleft()
    if x == 0 and ch[z]== 0 :
        ch[z]=1
        ans.append(z)
    if x+z <= a :
        q.append(x+z, y, 0)
    if x+z > a :
        q.append(a, y, z-a)
    if y+z <= b :
        q.append(x, y+z, 0)
    if y+z > b :
        q.append(x, b, z-b)
    
