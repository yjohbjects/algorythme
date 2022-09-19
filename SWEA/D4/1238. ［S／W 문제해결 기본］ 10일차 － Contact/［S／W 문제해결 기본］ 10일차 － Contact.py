def BFS(n):
    queue = [n]
    while queue:
        n = queue.pop(0)
        for contact in contacts[n]: #[7, 15]
            if visited[contact] == 0: # 방문한 적 없다면
                queue.append(contact)
                visited[contact] = visited[n] + 1
                # print(visited)


T = 10
for t in range(1, T+1):
    N, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    contacts = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]

    for i in range(N//2):
        fr = from_to[i * 2]
        to = from_to[i * 2 + 1]
        contacts[fr].append(to)

    visited[start] = 1
    BFS(start)

    maxV = 0
    result = 0
    for i in range(len(visited)):
        if visited[i] >= maxV:
            maxV = visited[i]
            result = i
    # print(visited)
    print(f'#{t} {result}')