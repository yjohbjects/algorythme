N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(len(A)):
    answer += A[i] * B[i]

print(answer)