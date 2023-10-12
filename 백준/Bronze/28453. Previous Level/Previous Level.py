N = int(input())

levels = list(map(int, input().split()))

answer = []
for level in levels:
    if level == 300:
        answer.append(1)
    elif level >= 275:
        answer.append(2)
    elif level >= 250:
        answer.append(3)
    else:
        answer.append(4)

print(*answer)