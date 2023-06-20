import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())

    nodes = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b  = map(int, sys.stdin.readline().split())
        nodes[a].append(b)
        nodes[b].append(a)
    
    colors = [0 for _ in range(V + 1)]

    def BFS(x):
        Q = deque([])
        Q.append(x) 

        colors[x] = 1 # 1 = red, 2 = blue
        while Q:
            x = Q.popleft()

            for y in nodes[x]:
                if colors[y] == 0:
                    Q.append(y)
                    colors[y] = 3 - colors[x]

    for i in range(1, V + 1):
        if colors[i] == 0:
            BFS(i)

    flag = True
    for i in range(1, V + 1):
        for j in nodes[i]:
            if colors[i] == colors[j]:
                flag = False
    print('YES' if flag else 'NO')
    