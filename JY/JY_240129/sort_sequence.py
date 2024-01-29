import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b=sorted(a)
ans=[]
for i in a :
    for j in range(n) :
        if i == b[j] :
            ans.append(j)
            b[j]=None
print(ans)