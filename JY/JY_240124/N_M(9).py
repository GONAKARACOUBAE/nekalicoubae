def sequence(n, m, seq, arr, j, ea, ch) :
    if ea==m :
        global cnt
        cnt+=1
        for i in range (m) :
            ans[cnt][i]=arr[i]
        return 0
    else :
        for i in seq :
            if ch[i] >= 1 :
                arr.append(i)
                ch[i]-=1
                sequence(n, m, seq, arr, i+1, ea+1, ch)
                ch[i]+=1
                arr.pop()
n, m = map(int, input().split())
seq=list(map(int, input().split()))
seq.sort()
cnt=0
ch=[0]*10001
ans=[[0] for j in range(2000) for i in range(9)]
for i in seq :
    ch[i]+=1
sequence(n, m, seq, [], 0, 0, ch)