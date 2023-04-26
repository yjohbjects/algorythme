word = input()

answer = []

temp = ''
for i in range(len(word)-1, -1, -1):
    temp = word[i] + temp
    answer.append(temp)

answer.sort()
print(*answer, sep='\n')