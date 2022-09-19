N = int(input())
words = []
for _ in range(N):
    temp = input()
    if temp not in words:
        words.append(temp)


words = sorted(words)
words = sorted(words, key=len)
print(*words, sep='\n')