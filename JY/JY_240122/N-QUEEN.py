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
def queen(arr, i, j, num, cnt) :
    global ans
    if cnt==num :
        ans+=1
        return 0
    while True : 
        if j<=num :
            j+=1
        if j>num :
            i+=1
            j=1
        if i>num :
            break
        if arr[i][j]==0 :
            arr = ch_queen(arr, i, j, num)
            queen(arr, i+1, j+1, num, cnt+1)
            arr = dch_queen(arr, i, j, num)
ans=0
n=int(input())
i=0
j=0
chess=[[0 for j in range(n+1)] for i in range(n+1)]
queen(chess,1, 0, n, 0)
print(ans)