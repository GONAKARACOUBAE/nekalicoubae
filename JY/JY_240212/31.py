answer = []
score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
mean=[]
for i in score :
    mean.append(sum(i))
result=sorted(mean, reverse=True)
for i in mean :
    answer.append(result.index(i)+1)
print(answer)