import sys
from collections import defaultdict
n = int(sys.stdin.readline())
arr= list(sys.stdin.readline().split())
low=high=0
uni=arr[0]+','
dic=defaultdict(int)
dic[uni]=1
while low<n :
    if high < n :
        high+=1
        if high==n :
            continue
        uni=uni+arr[high]+','
        dic[uni]=1
    else :
        low+=1
        high=low
        if low==n :
            continue
        uni=arr[low]+','
        dic[uni]=1
print(len(dic))