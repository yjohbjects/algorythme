T = int(input())
for t in range(T):
    words = list(map(str, input().split()))

    for i, word in enumerate(words):
        word = word[::-1]
        words[i] = word

    print(*words)