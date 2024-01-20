n=int(input())
switch=0
for i in range(n) :
    ps=input()
    switch=0
    ch=[0]*2
    for j in range(len(ps)) :
        if ps[j]=='(' :
            ch[0]+=1
        else :
            ch[1]+=1
        if ch[0]>=1 and ch[1]>=1 :
            ch[0]-=1
            ch[1]-=1
        elif ch[0]<1 and ch[1]>=1 :
            switch=1
            break
    if switch ==1 or ch[0]+ch[1]>0 :
        print('NO')
    elif switch ==0 and ch[0]+ch[1]==0 :
        print('YES')