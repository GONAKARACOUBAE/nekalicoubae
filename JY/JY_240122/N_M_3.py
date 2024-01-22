def seq(limit, ea, cnt, arr, now_value) :
    if now_value>limit :
        cnt=0
        arr=[]
        seq(limit, ea, cnt, arr, now_value+1)
    if cnt<ea :
        arr.append(now_value)
        seq(limit, ea, cnt+1, arr, now_value)
    else :
        print(arr)
        arr.pop()
        seq(limit, ea, cnt-1, arr, now_value+1)
m, n = map(int, input().split())
a=[]
seq(m, n, 0, a, 1)
