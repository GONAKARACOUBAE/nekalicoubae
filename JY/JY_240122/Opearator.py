def cal(ea, arr, operator, max, min, value, order) :
    global ans
    if order == n :
        if max < value :
            max = value
            ans[0]=max
        if min > value :
            min = value
            ans[1]=min
        return 0
    else :
        if operator[0] > 0 :
            operator[0]-=1
            cal(ea, arr, operator, max, min, value+arr[order], order+1)
        elif operator[1] > 0 :
            operator[1]-=1
            cal(ea, arr, operator, max, min, value-arr[order], order+1)
        elif operator[2] > 0 :
            operator[2]-=1
            cal(ea, arr, operator, max, min, value*arr[order], order+1)
        elif operator[3] > 0 :
            operator[3]-=1
            if value>0 :
                cal(ea, arr, operator, max, min, int(value/arr[order]), order+1)
            else :
                temp = value * -1
                temp = int(temp / arr[order])
                cal(ea, arr, operator, max, min, temp, order+1)

n=int(input())
a=list(map(int, input().split()))
ope=list(map(int, input().split()))
ans=[0]*3
cal(n, a, ope, 0, 2147483647, a[0], 1)
print(ans[0])
print(ans[1])