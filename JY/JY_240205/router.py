import sys
x=[]
n, c = map(int, sys.stdin.readline().split())
for i in range(n) :
    x.append(int(sys.stdin.readline().rstip()))
x.sort()
search()