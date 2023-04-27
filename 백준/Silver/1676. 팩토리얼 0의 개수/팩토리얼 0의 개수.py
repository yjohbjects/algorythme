import math

N = int(input())

temp = str(math.factorial(N))
answer = 0
for i in range(len(temp)-1, -1, -1):
    if temp[i] == '0':
        answer += 1
    else:
        break

print(answer)