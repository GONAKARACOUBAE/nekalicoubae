def seq(limit, ea, now_value, now_ea, arr, ch) :
    if now_ea>=ea :
        for i in range(limit+1) :
            if ch[i]>1 :
                return 0
        for i in range(ea) :
            print(a[i], end=" ")
        print()
        return 0
    else :
        for i in range(1, limit+1) :
            arr.append(i)
            ch[i]+=1
            seq(limit, ea, i, now_ea+1, arr, ch)
            arr.pop()
            ch[i]-=1
            

m, n = map(int, input().split())
a=[]
ch=[0]*10
seq(m, n, 0, 0, a, ch)
