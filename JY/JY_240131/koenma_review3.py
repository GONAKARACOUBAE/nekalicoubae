import sys
class Elem() :
    def __init__(self, name, korean, english, math) :
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

n = int(sys.stdin.readline())
arr=[]
for i in range(n) :
    inp=sys.stdin.readline().split()
    inp[1:]=map(int, inp[1:])
    arr.append(Elem(*inp))
ans = sorted(arr, key = lambda x : (-x.korean, x.english, -x.math, x.name))
names = [x.name for x in ans]
for i in names :
    print(i)