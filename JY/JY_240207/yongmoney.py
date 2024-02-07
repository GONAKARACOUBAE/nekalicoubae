import sys
sys.setrecursionlimit(10**6)
def ch(x, target) :
    global mc
    mc=1
    value=x
    for i in arr :
        if value < i :
            value+=x
            mc+=1
        value-=i
        if mc>target :
            return 0
    return mc
        
def search(low, high,target) :
    global ans
    mid = (low+high)//2
    if ch(mid, target) <= target :
        if mid < ans :
            ans = mid
        return -1
    elif ch(mid, target) < target :
        return search(low, mid-1, target)
    else :
        return search(mid+1, high, target)


n, m =map(int, sys.stdin.readline().split())
arr=[]
mc=0
ans=sys.maxsize
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
search(1, max(arr)*2, m)
print(ans)