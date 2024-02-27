
n=[]
n=input().split()
print(len(n))

arr = [list(map(int, input().split())) for i in range(3)]
arr2 = [list(map(int, input().split())) for i in range(3)]

arr3=arr+arr2
print(arr3)