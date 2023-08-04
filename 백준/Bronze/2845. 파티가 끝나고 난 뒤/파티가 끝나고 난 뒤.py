N, M = map(int, input().split())

people = N * M

guess = list(map(int, input().split()))
answer = []

for area in guess:
    answer.append(area - people)

print(*answer)