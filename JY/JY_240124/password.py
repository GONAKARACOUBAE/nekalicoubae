def ch_vowels(alpha) :
    if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' :
        return 1
    return 0
def ch_pass(l, c, al_list, arr, ea, j, vowels, constants) :
    if ea == l :
        if vowels >= 1 and constants >=2 :
            for i in range (l) :
                print(arr[i], end="")
            print()
    else :
        for i in range(j, c) :
            arr.append(al_list[i])
            if ch_vowels(al_list[i]) == 1 :
                vowels += 1
            else :
                constants+=1
            ch_pass(l, c, al_list, arr, ea+1, i+1, vowels, constants)
            arr.pop()
            if ch_vowels(al_list[i]) == 0 :
                vowels-=1
            else :
                constants-=1
l, c = map(int, input().split())
al_list = input().split()
al_list.sort()
arr=[]
ch_pass(l, c, al_list, arr, 0, 0, 0, 0)
