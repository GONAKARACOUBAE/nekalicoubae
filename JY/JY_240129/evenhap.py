import sys
answer=0
n=int(sys.stdin.readline())
for i in range(0, n+1, 2) :
    answer+=i
print(answer)