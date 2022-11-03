# B1932 정수 삼각형
# https://www.acmicpc.net/problem/1932

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(len(triangle[i])):
        if j == 0: # first val
            triangle[i][j] += triangle[i-1][j]

        elif j == len(triangle[i]) - 1: # last val
            triangle[i][j] += triangle[i-1][-1]

        else: # mid val
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


print(max(triangle[-1]))
