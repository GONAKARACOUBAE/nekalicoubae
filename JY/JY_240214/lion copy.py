import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ind_list = list(filter(lambda x : arr[x] == 1, range(len(arr))))
low=0
high=k-1
ans=sys.maxsize
if n==1 :
    if arr[0]==1 :
        print(1)
    else :
        print(-1)
elif k > len(ind_list) :
    print(-1)
else :
    while True :
        if high==len(ind_list) :
            break
        hap=ind_list[high]-ind_list[low]
        if hap < ans :
            ans=hap+1
        high+=1
        low+=1
    print(ans)
    

        