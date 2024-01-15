phone=input()
'''
rows = 1000001
cols = 2
cnt = 0
bi = 0
i=0
j=0
k=0
ch = [[0 for j in range(cols)] for i in range(rows)]
for i in phone_book : # 포문 쓰는법 잘 알기
    print(i)
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
'''
# 정확도 67, 시간 0점 효율적인 방법 연구
answer=True
    rows = 1000001
    cols = 21
    cnt = 0
    bi = 0
    i=0
    j=0
    cnt=0
    ch = [[0 for j in range(cols)] for i in range(rows)]
    for i in phone_book :
        a=list(i)
        for j in range(0, len(i)) :
            ch[cnt][j]=int(a[j])
        cnt+=1
    i=0
    j=0
    k=0
    x=0
    for i in range(0, cnt-1):
        for j in range(i+1, cnt) :
            for k in range(0, len(phone_book[i])) :
                if ch[i][k]!=ch[j][k] :
                    break
            if k==len(phone_book[i])-1 :
                x=1
                break
        if x==1 :
            break
    if x==1 :
        answer=False
    else :
        answer=True
    return answer