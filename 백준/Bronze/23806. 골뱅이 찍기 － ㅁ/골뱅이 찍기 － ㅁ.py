N = int(input())
for i in range(N):
    print('@' * (N * 5))

for i in range(N):
    print('@' * N + ' ' * (N * 3) + '@' * N)
    print('@' * N + ' ' * (N * 3) + '@' * N)
    print('@' * N + ' ' * (N * 3) + '@' * N)

for i in range(N):
    print('@' * (N * 5))