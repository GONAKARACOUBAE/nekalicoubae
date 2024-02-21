import sys
def search(start, end, hap) :
    global s
    global ans
    if hap == s :
        ans+=1
    if end+1<len(arr) :
        return search(start, end+1, hap+arr[end+1])
    else :
        if start+1<len(arr) :
            return search(start+1, start+1, arr[start+1])
        else :
            return 0
n, s = map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))
ans=0
search(0, 0, arr[0])
print(ans)