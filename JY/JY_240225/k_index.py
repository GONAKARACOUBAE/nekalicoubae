import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
b=[]
for i in range(1, n+1) :
    for j in range(1, n+1) :
        b.append(i*j)
b.sort()
print(b[m-1])