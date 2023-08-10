mbti = input()

N = int(input())

answer = 0
for _ in range(N):
    temp = input()

    if temp == mbti:
        answer += 1

print(answer)