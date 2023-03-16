S = int(input())

number = 0
answer = 0

i = 1
while True:
    if S - (number + i) > i:
        number += i
        answer += 1
    else:
        answer += 1
        break

    i += 1

print(answer)