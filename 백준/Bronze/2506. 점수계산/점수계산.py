N = int(input())
scores = map(int, input().split(' '))
answer = 0

temp = []
for score in scores:
    if score == 1:
        temp.append(temp)
        answer += len(temp)
    elif score == 0:
        temp = []

print(answer)

