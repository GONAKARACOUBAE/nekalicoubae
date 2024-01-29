import sys
n=int(input())
for i in range(n) :
    inp = sys.stdin.readline().split()
    inp[1:]= map(int, inp[1:])
print(inp)