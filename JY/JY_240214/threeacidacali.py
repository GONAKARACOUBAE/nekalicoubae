import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
ans=sys.maxsize
arr.sort()
res=[0]*3
for i in range(n-2) :
    low=i+1
    high=n-1
    if low==n-2 :
        hap = arr[low]+arr[high]+arr[i]
        if abs(hap) < ans :
            ans=abs(hap)
            res[0]=arr[i]
            res[1]=arr[low]
            res[2]=arr[high]
    else :
        while True :
            if low==high :
                break
            hap = arr[low]+arr[high]+arr[i]
            if abs(hap) < ans :
                ans=abs(hap)
                res[0]=arr[i]
                res[1]=arr[low]
                res[2]=arr[high]
            if hap > 0 :
                high-=1
            elif hap < 0 :
                low+=1
            else :
                res[0]=arr[i]
                res[1]=arr[low]
                res[2]=arr[high]
                break
for i in range(3) :
    print(res[i], end=' ')
            
    