score = {}
scores = []
for i in range(8):
    scores.append(int(input()))
    score[scores[-1]] = i+1

scores.sort()
print(scores[7] + scores[6] + scores[5] + scores[4] + scores[3])
questions = []

for j in range(3, 8):
    questions.append(score[scores[j]])

questions.sort()
print(*questions)