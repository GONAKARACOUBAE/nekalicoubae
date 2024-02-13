from collections import defaultdict
s='abcabcadc'
answer=''
k=''
dic=defaultdict(int)
for i in s :
    dic[i]+=1
for i in dic :
    if dic[i]==1 :
        k+=i
answer=''.join(sorted(k))
print(answer)

answer=''.join(sorted(ch for ch in s if s.count(ch) == 1))
