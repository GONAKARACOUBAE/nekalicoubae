my_str="abc1Addfggg4556b"
n=6
answer = []
cnt=0
for i in range(0, len(my_str), n) :
    answer.append(my_str[i:i+n])
print(answer)