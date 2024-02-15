import sys
def cut(x, t) :
    result=0
    for i in wood[::-1] :
        if i <= x :
            break
        result+=i-x

    return result
def parametric_search(low, high, target) :
    mid = (low+high)//2
    if cut(mid, target) == target :
        return mid
    elif cut(mid, target) > target :
        return parametric_search(mid+1, high, target)
    else :
        return parametric_search(low, mid-1, target)
n, m = map(int, sys.stdin.readline().split())
wood= list(map(int, sys.stdin.readline().split()))
wood.sort()
print(parametric_search(0, wood[len(wood)-1], m))