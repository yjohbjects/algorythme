T = int(input())

for z in range(T):
    word, key = map(str, input().split())
    cnt = 0

    while word.find(key) != -1:
        cnt += (len(word) - len(word.replace(key, ''))) // len(key)
        word = word.replace(key, '')
        break

    cnt += len(word)
    print(f'#{z+1} {cnt}')