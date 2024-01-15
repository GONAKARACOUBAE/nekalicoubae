def star(n): # 노가다하면서 찾은 규칙으로, 한방에 표현할 수 있을 것 같음. 변수들 간의 관계 정리해보기
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%3==2 and j%3==2:
                ch[i][j]=1
            if n>3 :
                if i%9 >=4 and i%9 <=6 and j%9 >=4 and j%9 <=6 :
                    ch[i][j]=1
            if n>9 :
                if i%27 >=10 and i%27 <=18 and j%27 >=10 and j%27 <=18 :
                    ch[i][j]=1
            if n>27 :
                if i%81 >=28 and i%81 <=54 and j%81 >=28 and j%81 <=54 :
                    ch[i][j]=1
            if n>81 :
                if i%243 >= 82 and i%81 <=162 and j%243 >=82 and j%243 <=162 :
                    ch[i][j]=1
            if n>243 :
                if i%729 >= 244 and i%729 <= 486 and j%729 >= 244 and j%729 <=486 :
                    ch[i][j]=1
            if n>729 :
                if i%2187 >=730 and i%2187 <=1458 and j%2187 >=730 and j%2187 <=1458 :
                    ch[i][j]=1
            if n>2187 :
                k=2187*3
                if i%k >= (int(k/2)+1)-(int(2187/2)) and i%k <= (int(k/2)+1)+(int(2187/2)) and j%k >= (int(k/2)+1)-(int(2187/2)) and j%k <=(int(k/2)+1)+(int(2187/2)) :
                    ch[i][j]=1
                
        
i=0
j=0                
n=int(input())
ch = [[0 for j in range(n+1)] for i in range(n+1)]
star(n)
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if ch[i][j]==0 :
            print('*',end='')
        else :
            print(' ', end='')
    print('\n')