# 1406 에디터

from collections import deque

stack = [char for char in input()]
queue = deque([])
N = int(input())

for _ in range(N):
    command = list(input().split())

    if command[0] == 'L': # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        if stack:
            queue.appendleft(stack.pop())

    elif command[0] == 'D': # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        if queue:
            stack.append(queue.popleft())

    elif command[0] == 'B': # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        if stack:
            stack.pop()

    else: # P 문자: command[1] 문자를 커서 왼쪽에 추가함
        stack.append(command[1])

print(''.join(stack) + ''.join(queue))