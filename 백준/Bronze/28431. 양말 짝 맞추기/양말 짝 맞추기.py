socks = []
answer = 0
for _ in range(5):
    socks.append(int(input()))

for sock in socks:
    if socks.count(sock) % 2 != 0:
        answer = sock

print(answer)