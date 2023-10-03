N = int(input())

answer = 0
for _ in range(N):
    a = input()
    
    if int(a[2:]) <= 90:
        answer += 1

print(answer)