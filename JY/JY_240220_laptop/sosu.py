scovile=[1,2,3,9,10,12]
k=7
answer=0
while True :
    answer+=1
    min1=min(scovile)
    scovile.remove(min1)
    min2=min(scovile)
    scovile.remove(min2)
    scovile.append(min1+min2*2)
    if min(scovile)>=k :
        break
    if answer==len(scovile)-1 :
        answer=-1
        break