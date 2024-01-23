def ch_queen(a, now_x, now_y, bound) :
    a[now_x][now_y]+=1
    for i in range(1,bound) :
        if now_y+i <=bound :
            a[now_x][now_y+i]+=1
        if now_x+i <=bound :
            a[now_x+i][now_y]+=1
        if now_x-i >=1 :
            a[now_x-i][now_y]+=1
        if now_y-i >=1 :
            a[now_x][now_y-i]+=1
        if now_x+i <=bound and now_y+i <=bound :
            a[now_x+i][now_y+i]+=1
        if now_x-i >=1 and now_y-i >=1 :
            a[now_x-i][now_y-i]+=1
        if now_x+i <= bound and now_y-i >=1 :
            a[now_x+i][now_y-i]+=1
        if now_x-i>=1 and now_y+i <= bound :
            a[now_x-i][now_y+i]+=1
    return a
def dch_queen(a, now_x, now_y, bound) :
    a[now_x][now_y]-=1
    for i in range(1,bound) :
        if now_y+i <=bound :
            a[now_x][now_y+i]-=1
        if now_x+i <=bound :
            a[now_x+i][now_y]-=1
        if now_x-i >=1 :
            a[now_x-i][now_y]-=1
        if now_y-i >=1 :
            a[now_x][now_y-i]-=1
        if now_x+i <=bound and now_y+i <=bound :
            a[now_x+i][now_y+i]-=1
        if now_x-i >=1 and now_y-i >=1 :
            a[now_x-i][now_y-i]-=1
        if now_x+i <= bound and now_y-i >=1 :
            a[now_x+i][now_y-i]-=1
        if now_x-i>=1 and now_y+i <= bound :
            a[now_x-i][now_y+i]-=1
    return a
def queen(arr, x, y, num, cnt) :
    global ans
    if cnt == 0 :
        arr = [[0 for j in range(n+1)] for i in range(n+1)]
    if cnt==num :
        ans+=1
    for i in range(1, num+1) :
        for j in range(1, num+1) :
            if arr[i][j]==0 :
                arr = ch_queen(arr, i, j, num)
                queen(arr, i, j, num, cnt+1)
                arr = dch_queen(arr, i, j, num)
ans=0
n=int(input())
i=0
j=0
queen(1, 1, 1, n, 0)
print(ans)