N = int(input())


for _ in range(N):
    print('@' * 3 * N + ' ' * N + '@' * N)

for _ in range(N):
    print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)
    print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)
    print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)

for _ in range(N):
    print('@' * N + ' ' * N + '@' * 3 * N)