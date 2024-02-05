import sys
n , m = map(int, sys.stdin.readline().split())
hear=set()
see=set()
for i in range(n):
    hear.add(sys.stdin.readline().rstrip())
for j in range(m) :
    see.add(sys.stdin.readline().rstrip())
ans = list(hear & see)
ans.sort()
print(len(ans))
for i in range(len(ans)): 
    print(ans[i])
