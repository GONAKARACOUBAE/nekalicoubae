def dup(ans, arr) :
    for i in range(cnt) :
        if ans[i]==arr :
            return 1
    return 0
def sequence(n, m, seq, arr, ea, ch) :
    if ea==m :
        global cnt
        if dup(ans, arr) == 0 :
            for i in range (m) :
                ans[cnt][i]=arr[i]
            cnt+=1
        return 0
    else :
        for i in seq :
            if ch[i] >= 1 :
                arr.append(i)
                ch[i]-=1
                sequence(n, m, seq, arr, ea+1, ch)
                ch[i]+=1
                arr.pop()
n, m = map(int, input().split())
seq=list(map(int, input().split()))
seq.sort()
cnt=0
ch=[0]*10001
ans=[[0 for j in range(m)] for i in range(1000000)]
for i in seq :
    ch[i]+=1
sequence(n, m, seq, [], 0, ch)
for i in range(cnt) :
    print(ans[i])