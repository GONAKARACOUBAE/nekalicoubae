import sys
n=int(sys.stdin.readline().rstrip())
word=[]
for i in range(n): 
    word.append(sys.stdin.readline().rstrip())
word=dict.fromkeys(word)
ans=sorted(word, key = lambda x: (len(x), x))
for i in ans :
    print(i)
