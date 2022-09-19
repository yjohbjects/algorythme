T = int(input())

for t in range(1, T+1):
    result = []
    words = list(map(str, input().split()))

    while words:
        result.append(words.pop())

    print(f'Case #{t}:',  *result)