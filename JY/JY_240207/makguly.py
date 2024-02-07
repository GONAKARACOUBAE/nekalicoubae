import sys
def makguly(x) :
    ch=0
    global k
    for i in arr :
        if x !=0 :
            ch+=i//x
    if ch>=k :
        return True
    else :
        return False
def search(low, high) :
    global ans
    if low > high :
        return -1
    mid=(low+high)//2
    if makguly(mid) == True :
        if ans < mid :
            ans=mid
        return search(mid+1, high)
    else :
        return search(low, mid-1)

n, k = map(int, sys.stdin.readline().split())
arr=[]
ans=0
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
search(0, max(arr))
print(ans)