def cal(ea, arr, operator, value, order) :
    global ans
    if order == n :
        if ans[0] < value :
            ans[0]=value
        if ans[1] > value :
            ans[1]=value
        return 0
    else :
        if operator[0] > 0 :
            operator[0]-=1
            cal(ea, arr, operator, value+arr[order], order+1)
            operator[0]+=1
        if operator[1] > 0 :
            operator[1]-=1
            cal(ea, arr, operator,value-arr[order], order+1)
            operator[1]+=1
        if operator[2] > 0 :
            operator[2]-=1
            cal(ea, arr, operator, value*arr[order], order+1)
            operator[2]+=1
        if operator[3] > 0 :
            operator[3]-=1
            if value>0 :
                cal(ea, arr, operator,  int(value/arr[order]), order+1)
                operator[3]+=1
            else :
                temp = value * -1
                temp = int(temp / arr[order])
                temp = temp * -1
                cal(ea, arr, operator,  temp, order+1)
                operator[3]+=1

n=int(input())
a=list(map(int, input().split()))
ope=list(map(int, input().split()))
ans=[0]*3
ans[0]=-2147483640
ans[1]=2147483647
cal(n, a, ope, a[0], 1)
print(ans[0])
print(ans[1])