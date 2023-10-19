N = int(input())

answer = []

for _ in range(N):
    answer.append(int(input()))
    
print(*sorted(answer), sep='\n')