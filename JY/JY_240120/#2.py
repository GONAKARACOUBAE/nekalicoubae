def ch_prime() :
    global ch
    ch=[0]*(10**6)
    for i in range(2,10**6) :
        if ch[i]==0 :
            for j in range(i+i, 10**6, i) :
                ch[j]=1
def ch_num(now, order, cnt) :
    global answer, ch
    if ch[now]==0 :
        answer+=1
    if cnt==len(numbers) :
        return 0
    ch_num(now*10+int(numbers[order]), order+1, cnt+1)
    ch_num(int(numbers[order]), 0, 1)
    
answer=0
ch=[0]*(10**6)
ch_prime()
numbers=input()
ch[1]=ch[0]=1
ch_num(0, 0, 0)
print(answer)
