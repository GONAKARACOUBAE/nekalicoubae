answer=0
n=10
i=0
while i<n :
    answer+=1
    i+=1
    if answer%3 == 0 :
        i-=1
    elif '3' in str(answer) :
        i-=1
print(answer)