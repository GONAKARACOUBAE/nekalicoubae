num_list=input()
length=len(num_list)
i=1
ch=0
ans=[]
bef=None
now=0
for i in range(1,length,3) : # 다른 방식 찾기
    now=int(num_list[i])
    if bef!=now :
        ch=0
    if ch==0 :
        ans.append(now)
        ch=1
    bef=now
print(ans)

