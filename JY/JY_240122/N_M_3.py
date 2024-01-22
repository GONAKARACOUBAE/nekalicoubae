def seq(limit, ea, cnt, arr, now_value) :
    if cnt<ea and now_value <=limit :
        arr.append(now_value)
        seq(limit, ea, cnt+1, arr, now_value)
        print(arr)
        arr.pop()
        seq(limit, ea, cnt-1, arr, now_value+1)
m, n = map(int, input().split())
a=[]
seq(m, n, 0, a, 1)
