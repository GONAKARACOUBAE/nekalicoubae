def hap(start, end, value) :
    global length
    if start==len(sequence)-1 or end == len(sequence)-1 :
        return 0
    if value > k :
        return 0 
    if value==k :
        if length > end-start :
            global ans_s, ans_e
            ans_s=start
            ans_e=end
            length=end-start
    if end>=start:        
        hap(start, end+1, value+sequence[end+1])
        hap(start+1, end, value-sequence[start])
global sequence, length, k, ans_s, ans_e
ans_s=ans_e=0
length = 1000001
sequence=[1, 1, 1, 2, 3, 4, 5]
k=5
hap(0,0,sequence[0])
print(ans_s, ans_e)