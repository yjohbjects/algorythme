# B1158 요세푸스 문제

from collections import deque

N, K = map(int, input().split())
queue = deque([i + 1 for i in range(N)])
josephus = []

while queue:
    queue.rotate(-(K-1))
    josephus.append(queue.popleft())

print('<', end='')
print(*josephus, sep=', ', end='')
print('>')

