# B1872 스택 수열
# https://www.acmicpc.net/problem/1874

N = int(input())
result = []
for _ in range(N):
    result.append(int(input()))

stack = []
stack2 = []
answer = []
idx = 0
for i in range(1, N + 1):
    stack.append(i)
    answer.append('+')

    while stack and stack[-1] == result[idx]:
        stack2.append(stack.pop())
        answer.append('-')
        idx += 1

if result == stack2:
    for a in answer:
        print(a)
else:
    print('NO')