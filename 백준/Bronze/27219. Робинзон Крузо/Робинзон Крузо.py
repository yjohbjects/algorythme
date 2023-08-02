N = int(input())

answer = 'V' * (N // 5)
answer += 'I' * (N % 5)

print(answer)