def ch_queen (ch, x, y, cnt) :
    for i in range(cnt) :
        if x==ch[i][0] :
            return 0
        if y==ch[i][1] :
            return 0
        if x-y == ch[i][0]-ch[i][1] :
            return 0
        if x+y == ch[i][0]+ch[i][1] :
            return 0
    return 1
def queen(ch, i, j, cnt, num, switch) :
    global ans
    if switch==0 :
        if cnt == num :
            ans+=1
            switch=1
            return 0
        else :
            while True : 
                if j<num :
                    j+=1
                if j>=num :
                    i+=1
                    j=0
                if i==num :
                    break
                if ch_queen(ch, i, j, cnt) == 1 :
                    ch[cnt][0]=i
                    ch[cnt][1]=j
                    queen(ch, i, j, cnt+1, num, 0)
                    ch[cnt][0]=None
                    ch[cnt][1]=None
n=int(input())
ans=0
ch=[[None for j in range(2)] for i in range(n)]
queen(ch, 0, -1, 0, n, 0)
print(ans)