word = input().upper()

cnt = {}
for char in word:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1

maxV = 0
answer = ''
is_question = False
for v in cnt:
    if cnt.get(v) == maxV:
        answer = '?'
    elif cnt.get(v) > maxV:
        is_question = False
        maxV = cnt.get(v)
        answer = v

print(answer)