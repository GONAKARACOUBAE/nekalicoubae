def subsequence(n, s, num, hap, i) :
    if i==n :
        return 0
    else :
        for j in range(i, n) :
            hap+=num[j]
            if hap==s :
                global ans
                ans+=1
            subsequence(n, s, num, hap, j+1)
            hap-=num[j]
ans=0
n, s = map(int,input().split())
num=list(map(int, input().split()))
subsequence(n, s, num, 0, 0)
print(ans)