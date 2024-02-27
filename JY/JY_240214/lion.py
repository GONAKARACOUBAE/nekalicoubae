import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
if k == 1 and arr[0] == 1 :
    print(1)
else :
    low=0
    high=1
    ch=0
    ans=-1
    if arr[0] == 1 :
        ch+=1
    if arr[1] == 1 :
        ch+=1
    while True :
        if ch == k and ans < (high-low+1) :
            ans=(high-low+1)
        while True :
            high+=1
            if arr[high]==1 :
                ch+=1
                break
        if ch>k :
            while True :
                low+=1
                if arr[low]==1 :
                    ch-=1
                    break
        