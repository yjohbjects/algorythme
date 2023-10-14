N = int(input())

answer = 0
for _ in range(N):
    a = int(input())
    answer += a
   
print(answer-(N-1))