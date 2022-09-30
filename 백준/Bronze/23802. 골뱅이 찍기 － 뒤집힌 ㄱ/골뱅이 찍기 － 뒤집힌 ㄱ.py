N = int(input())

for i in range(N):
    print('@' * (5 * N))

for i in range(N):
    for j in range(4):
        print('@' * N)