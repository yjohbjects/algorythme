import sys


n, m = map(int, sys.stdin.readline().split())

dict = {}
for _ in range(n):
    dict[sys.stdin.readline()] = 0

answer = []
for _ in range(m):
    name = sys.stdin.readline()
    if name in dict:
        answer.append(name.strip('\n'))

answer.sort()
print(len(answer))
print(*answer, sep='\n')

