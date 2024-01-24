def ch_vowels(alpha) :
    if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' :
        return 1
    return 0
def ch_pass(l, c, al_list, arr, ea, ch, vowels) :
    if ea == l :
        if vowels == 1 :
            print(arr)
    else :
        for i in range(c) :
            if ch[ord(al_list[i])] == 0 :
                arr.append(al_list[i])
                ch[ord(al_list[i])]=1
                if ch_vowels(al_list[i]) == 1 :
                    vowels = 1
                ch_pass(l, c, al_list, arr, ea+1, ch, vowels)
                arr.pop()
                ch[ord(al_list[i])]=0
l, c = map(int, input().split())
al_list = input().split()
al_list.sort()
arr=[]
ch=[0]*180
ch_pass(l, c, al_list, arr, 0, ch, 0)
