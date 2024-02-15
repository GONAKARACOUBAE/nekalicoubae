import sys
sys.setrecursionlimit(10**6)
def duo(low, high, target) :
    global ans
    if low!=high :
        if a[low]+a[high] == target :
            ans+=1
        if a[low]+a[high] < target :
            return duo(low+1, high, target)
        else :
            return duo(low, high-1, target)
    else :
        return 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
ans=0
a.sort()
duo(0, len(a)-1, x)
print(ans)