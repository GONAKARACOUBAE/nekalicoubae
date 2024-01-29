import sys
import math
n=int(sys.stdin.readline())
ch=[0]*((2**63)-1)
switch=-1
max=-math.inf
for i in range(n) :
    card=int(sys.stdin.readline())
    if card >= 0 :
        ch[card]+=1
        if ch[card]>max :
            max=ch[card]
            ind=card    
    else :
        ch[(card*-1)+2**62]+=1
        if ch[card+2**62]>max :
            max=ch[card+2**62]
            ind=card+2**62
if ind>2**62 :
    print((ind-2**62)*-1)
else :
    print(ind)

