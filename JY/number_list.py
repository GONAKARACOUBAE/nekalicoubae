phone=input()
rows = 1000001
cols = 2
cnt = 0
bi = 0
i=0
j=0
k=0
ch = [[0 for j in range(cols)] for i in range(rows)]
for i in range(1, len(phone)) :
    if phone[i]=='"' :
        ch[cnt][bi]=i
        if bi == 0 :
            bi = 1
        elif bi == 1 :
            bi = 0
            cnt+=1
i=0
j=0
k=0
x=0            
print(cnt)
print(ch)
for i in range(0, cnt-1):
    for j in range(i+1, cnt) :
        for k in range(1, ch[i][1]-ch[i][0]) :
            if phone[k+ch[i][0]]!=phone[k+ch[j][0]] :
                break
        if k==ch[i][1]-ch[i][0]-1 :
            x=1
            break
    if x==1 :
        break
if x==1 :
    print('false')
else :
    print('true')