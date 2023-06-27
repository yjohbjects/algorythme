calc = list(input().split('-'))

for i in range(len(calc)):
    if '+' in calc[i]:
        calc[i] = sum(list(map(int, calc[i].split('+'))))

answer = int(calc[0])
for i in range(1, len(calc)):
    num = int(calc[i])
    answer -= int(calc[i])

print(answer)