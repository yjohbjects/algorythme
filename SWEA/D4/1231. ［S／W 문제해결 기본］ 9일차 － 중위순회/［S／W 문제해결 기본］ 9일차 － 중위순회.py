def inorder(node):
    global result
    if node != 0:
        # 왼쪽 먼저 방문
        inorder(tree[node][0])
        result += tree[node][1]
        # return(f'{tree[node][1]}')
        # 오른쪽 방문
        inorder(tree[node][2])

for t in range(10):
    V = int(input())
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]

    for _ in range(V):
        temp = list(map(str, input().split()))
        tree[int(temp[0])][1] = temp[1]

        if len(temp) >= 3:
            tree[int(temp[0])][0] = int(temp[2])
        if len(temp) >= 4:
            tree[int(temp[0])][2] = int(temp[3])

    result = ''
    inorder(1)
    print(f'#{t+1}', result)
