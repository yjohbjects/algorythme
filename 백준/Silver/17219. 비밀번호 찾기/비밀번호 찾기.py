N, M = map(int, input().split(' '))

pws = {}
answer = []
for _ in range(N):
    site, pw = input().split(' ')
    pws[site] = pw

for _ in range(M):
    answer.append(pws.get(input()))

print(*answer, sep="\n")