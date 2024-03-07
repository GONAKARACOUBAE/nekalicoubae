import sys
sys.setrecursionlimit(10**9)
def search(low, high, hap, target) :
    global ans
    global n
    if low>high :
        return 0
    if hap == target :
        ans+=1
    if hap > target :
        return search(low+1, high, hap-a[low], target)
    else :
        if high+1 == n :
            return search(low+1, high, hap-a[low], target)
        else :
            return search(low, high+1, hap+a[high+1], target)
n, m = map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
ans=0
search(0, 0, a[0], m)
print(ans)