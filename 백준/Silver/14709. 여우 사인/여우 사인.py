N = int(input())

nodes = [[i] for i in range(6)]

for _ in range(N):
    a, b = map(int, input().split())

    nodes[a].append(b)
    nodes[b].append(a)

nodes[1].sort()
nodes[3].sort()
nodes[4].sort()

if nodes[2] != [2] or nodes[5] != [5]:
    print('Woof-meow-tweet-squeek')

elif 2 in nodes[1] or 5 in nodes[1]or 2 in nodes[3] or 5 in nodes[3] or 2 in nodes[4] or 5 in nodes[4]:
    print('Woof-meow-tweet-squeek')

elif nodes[1] == nodes[3] == nodes[4] and len(nodes[1]) == 3:
    print('Wa-pa-pa-pa-pa-pa-pow!')

else:
    print('Woof-meow-tweet-squeek')