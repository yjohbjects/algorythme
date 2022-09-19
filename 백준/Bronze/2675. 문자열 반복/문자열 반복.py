T = int(input())
for t in range(T):
    N, word = map(str, input().split())
    result = ''
    for char in word:
        result += char * int(N)

    print(result)
