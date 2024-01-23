def test(arr) :
    for i in range (4) :
        for j in range(4) :
            arr[i][j]+=1
            test(arr)
n= 4
a = [[0 for j in range(n+1)] for i in range(n+1)]
test(a)