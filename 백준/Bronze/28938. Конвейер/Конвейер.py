N = int(input())

answer = 0
moves = list(map(int, input().split()))

temp = sum(moves)

if temp == 0:
    print('Stay')
elif temp > 0:
    print('Right')
else:
    print('Left')