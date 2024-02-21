import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
arr=list(map(str,sys.stdin.readline().split()))
arr.sort()
for i in combinations(arr, l) :
    mo=0
    ja=0
    for j in i :
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' :
            mo=1
        else :
            ja+=1
    if mo==1 and ja>=2 :
        print(''.join(i))