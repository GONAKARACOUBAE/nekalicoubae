def ch_vowels(alpha) :
    if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' :
        return 1
    return 0
def ch_pass(l, c, al_list, arr, ea, j, vowels) :
    if ea == l :
        if vowels == 1 :
            for i in range (l) :
                print(arr[i], end="")
            print()
    else :
        for i in range(j, c) :
            arr.append(al_list[i])
            if ch_vowels(al_list[i]) == 1 :
                vowels = 1
            ch_pass(l, c, al_list, arr, ea+1, i+1, vowels)
            arr.pop()
l, c = map(int, input().split())
al_list = input().split()
al_list.sort()
arr=[]
ch=[0]*180
ch_pass(l, c, al_list, arr, 0, 0, 0)
