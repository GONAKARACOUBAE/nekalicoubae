def seq(limit, ea, now_value, now_ea, arr) :
    if now_ea==ea :
        for i in range(ea) :
            print(a[i], end=" ")
        print()
    for i in range(1, limit+1) :
        if i>now_value :
            arr.append(i)
            seq(limit, ea, i, now_ea+1, arr)
            arr.pop()

m, n = map(int, input().split())
a=[]
seq(m, n, 0, 0, a)