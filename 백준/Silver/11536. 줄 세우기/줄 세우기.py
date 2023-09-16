N = int(input())

players = []

for _ in range(N):
    players.append(input())

increasing = sorted(players)
decreasing = sorted(players, reverse=True)

if players == increasing:
    print('INCREASING')
elif players == decreasing:
    print('DECREASING')
else:
    print('NEITHER')