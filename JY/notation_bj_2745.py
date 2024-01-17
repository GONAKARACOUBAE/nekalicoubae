n, b = map(str, input().split())
b=int(b)
cnt=0
ans=0
for i in range(len(n)-1, -1, -1) :
    ans+=(ord(n[i])-55)*(b**cnt)
    cnt+=1
print(ans)
