import sys

ans={}

n=int(sys.stdin.readline())
for i in range(n) :
    num=input()
    if (num in ans) == False :
        ans[num]=1
    else :
        ans[num]+=+1
print(ans)