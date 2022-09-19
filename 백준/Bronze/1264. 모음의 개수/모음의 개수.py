while True:
    sentence = input()
    if sentence == '#':
        break
    else:
        cnt = 0
        for char in sentence:
            if char in 'aeiouAEIOU':
                cnt += 1
            else:
                continue
        print(cnt)