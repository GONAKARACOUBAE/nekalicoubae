import sys
my_string=sys.stdin.readline().rstrip()
letter=sys.stdin.readline().rstrip()
ans=''
for i in my_string :
    if i != letter :
        ans+=i
print(ans)