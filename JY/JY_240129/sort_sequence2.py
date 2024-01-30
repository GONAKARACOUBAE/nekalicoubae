import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b=sorted(a)
ans=[]
for i in a :
    print(b.index(i), end=" ")
    b[b.index(i)]=None