poly = "25x + 1"
arr = poly.split(' + ')
x_cnt=0
num=0
print(arr[0].index('x'))
for i in arr :
    if ('x' in i) == True :
        if i == 'x' :
            x_cnt+=1
        else :
            x_cnt+=int(i[0])
    else :
        num+=int(i)
if x_cnt > 0 and num > 0 :
        if x_cnt == 1 :
            answer='x'+' + ' + str(num)
        else :
            answer=str(x_cnt)+'x'+' + ' + str(num)
elif num == 0 :
    if x_cnt > 1 :
        answer=str(x_cnt)+'x'
    else :
        answer='x'
else :
    answer=str(num)
print(answer)