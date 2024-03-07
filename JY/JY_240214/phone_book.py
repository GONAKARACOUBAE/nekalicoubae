phone_book=["119", "97674223", "1195524421"]
answer=True
ch=0
for i in range(len(phone_book)) :
    for j in range(i+1, len(phone_book)) :
        if phone_book[j].find(phone_book[i]) == 0 :
            ch=1
            answer=False
            break
    if ch == 1 :
        break
print(answer)