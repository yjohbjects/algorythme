# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.

L = int(input())
S = list(map(int, input().split()))
S.append(0)
n = int(input())

S.sort()
answer = 0
for i in range(L):
    if S[i] < n < S[i+1]:
        for j in range(S[i] + 1, n + 1):
            if j == n:
                answer += ((S[i+1] - 1) - j)
            else:
                answer += ((S[i+1] - 1) - j) - (n - j - 1)
    else:
        continue
    
print(answer)