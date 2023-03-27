answer = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        answer += 40
    else:
        answer += score

print(answer//5)