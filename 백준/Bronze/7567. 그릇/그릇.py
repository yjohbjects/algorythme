plates = input()

answer = 0

stack = []
for plate in plates:
    if not stack or plate != stack[-1]:
        answer += 10
    else:
        answer += 5
    stack.append(plate)

print(answer)