import sys
from itertools import permutations
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ch=defaultdict(int)
for i in permutations(arr, m) :
    if m==1 :
        if ch[i[0]]!=1 :
            print(i[0])
            ch[i[0]]=1 
    else :
        if ch[' '.join(map(str, i))]!=1 :
            print(' '.join(map(str, i)))
            ch[' '.join(map(str, i))]=1
        

           