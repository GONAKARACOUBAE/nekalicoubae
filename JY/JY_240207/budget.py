import sys
def ch(x) :
    now=0
    global m
    for i in budget :
        if i < x :
            now+=i
        else :
            now+=x
        if now > m :
            return False
    return True
def search(low, high, target) :
    global ans
    if low > high :
        return -1
    mid=(low+high)//2
    if ch(mid) == True :
        ans=mid
        search(mid+1, high, target)
    else :
        search(low, mid-1, target)

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ans = 0
budget.sort()
search(budget[0], budget[n-1], m)
print(ans)