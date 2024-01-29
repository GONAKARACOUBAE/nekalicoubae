import sys

ans={}

n=int(sys.stdin.readline())
for i in range(n) :
    num=int(input())
    if (num in ans) == False :
        ans[num]=1
    else :
        ans[num]+=+1
sorted_ans = sorted(ans.items(), key = lambda item: (-item[1], item[0]))
print(sorted_ans[0][0])