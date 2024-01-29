import sys

ans={}

n=int(sys.stdin.readline())
for i in range(n) :
    num=input()
    if (num in ans) == False :
        ans[num]=1
    else :
        val=ans.get(num)
        ans[num]=val+1
print(ans)