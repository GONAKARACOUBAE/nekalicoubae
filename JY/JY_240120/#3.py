scovile=[1,2,3,9,10,12]
ch=[0]*1000001
k=7
cnt=0
ans=0
switch=0
b=0
a=0
for i in scovile :
    if i < k :
        ch[i]+=1
i=0
while i<k :
    i+=1
    if ch[i]>0 :
        ch[i]-=1
        a=b
        b=i
        i-=1
        
        
        cnt+=1
        if cnt%2 ==0 :
            ch[a]-=1
            ch[b]-=1
            ch[b*2+a]+=1
            ans+=1
for i in range(k) :
    if ch[i] > 0 :
        switch=1
        print(-1)
        break
if switch==0 :
    print(ans)