def ch_prime() :
    global ch
    ch=[0]*(10**6)
    for i in range(2,10**6) :
        if ch[i]==0 :
            for j in range(i+i, 10**6, i) :
                ch[j]=1
def ch_num() :
    ch_num
answer=0
ch=[0]*(10**6)
index=[]
num_list=[0]*10
ch_prime()
numbers=input()
for i in numbers :
    if num_list[int(i)] == 0 :
        index.append(i)
    num_list[int(i)]+=1
ch[1]=ch[0]=1
ch_num(0)
print(answer)
