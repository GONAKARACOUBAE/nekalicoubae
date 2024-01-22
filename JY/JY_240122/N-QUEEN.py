def ch_queen(a, now_x, now_y, bound) :
    for i in range(bound) :
        if now_y+i <=bound :
            a[now_x][now_y+i]=1
        if now_x+i <=bound :
            a[now_x+i][now_y]=1
        if now_x-i >=1 :
            a[now_x-i][now_y]=1
        if now_y-i >=1 :
            a[now_x][now_y-i]=1
        if now_x+i <=bound and now_y+i <=bound :
            a[now_x+i][now_y+i]=1
        if now_x-i >=1 and now_y-i >=1 :
            a[now_x-i][now_y-i]=1
    return a
def queen(arr, x, y, num, cnt) :
    global ans
    if cnt==num :
        ans+=1
    if arr[x][y]==0 :
        arr=ch_queen(arr, x, y, num)
    if y+1 <= num :
        queen(arr,x,y+1,num, cnt+1)
    elif x+1 <= num :
        queen(arr, x+1, 1, num, cnt+1)    
ans=0
n=int(input())
i=0
j=0
chess = [[0 for j in range(n+1)] for i in range(n+1)]

queen(chess, 1, 1, n, 0)
print(ans)