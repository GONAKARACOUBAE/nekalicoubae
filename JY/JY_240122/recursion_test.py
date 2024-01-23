def test(arr) :
    for i in range (4) :
        if arr[i]<2 :
            arr[i]+=1
            test(arr)
n= 4
a = [0]*5
test(a)