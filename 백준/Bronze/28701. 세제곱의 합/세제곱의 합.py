num = int(input())

answer = 0

for i in range(1, num + 1):
    answer += i

print(answer)

print(answer ** 2)

answer = 0

for i in range(1, num + 1):
    answer += i ** 3

print(answer)