from collections import deque

for t in range(10):
    T = int(input())
    numbers = deque(map(int, input().split()))



    cycle = [1, 2, 3, 4, 5]
    x = 0
    while True:
        # print(cycle[x%6])
        if numbers[0] - cycle[x%5] > 0:
            numbers.append(numbers.popleft() - cycle[x%5])
        else:
            numbers.popleft()
            numbers.append(0)
            break
        x += 1

    print(f'#{T}', *numbers)