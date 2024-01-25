def binary_search(x, btree) :
    global ch
    if ch==0 :
        if len(btree)>=1 :
            hap=0
            for i in range(len(btree)) :
                hap+=btree[i]*(2**(len(btree)-i-1))
                if hap == x :
                    ch=1
                    return 0
                elif hap > x :
                    return 0-p----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if ch==1 :
            return 0
        btree.append(1)
        binary_search(x, btree)
        if ch==1 :
            return 0
        btree.pop()
        btree.append(0)
        binary_search(x, btree)
        btree.pop()
        if ch==1 :
            return 0
    else :
        return 0
global ch
arr=[]
ans=[]
numbers=[7, 42, 5]
for i in numbers :
    ch=0
    arr=[]
    binary_search(i, arr)
    if ch==1 :
        ans.append(1)
    else :
        ans.append(0)
print(ans)