import sys
from collections import defaultdict
n = int(sys.stdin.readline())
arr=sys.stdin.readline().rstrip()
low=0
high=0
dic=defaultdict(int)
dic[arr[0]]=1
ans=1
while True : 
    high+=1
    dic[arr[high]]+=1
    if arr[high]!=arr[high-1] :
        if len(dic) > n :
            if ans < high-low :
                ans = high-low
            while True :
                dic[arr[low]]-=1
                if dic[arr[low]] ==0 :
                    del(dic[arr[low]])
                    low+=1
                    break
                low+=1
    if high == len(arr)-1 :
        break
    if low == len(arr)-1 :
        break
print(ans)