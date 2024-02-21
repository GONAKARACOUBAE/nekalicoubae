import sys
def search(start, end, hap) :
    global s
    global ans
    if hap == s :
        ans+=1
    if end+1<len(arr) :
        search(start, end+1, hap+arr[end+1])
    else :
        
    
n, s = map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))
ans=0
search(0, 0, arr[0])
print(ans)