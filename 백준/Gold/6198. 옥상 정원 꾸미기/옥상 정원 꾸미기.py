N = int(input())

answer = 0
buildings = []
for _ in range(N):
    buildings.append(int(input()))

stack = []
for building in buildings:
    while stack and building >= stack[-1]:
        stack.pop()
    stack.append(building)
    answer += len(stack) - 1

print(answer)