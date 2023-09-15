N = int(input())

answer = 0
for i in range(1, N+1):
    temp = 0
    for j in range(i, N+1):
        temp += j

        if temp >= N:
            if temp == N:
                answer += 1
            break
    
print(answer)