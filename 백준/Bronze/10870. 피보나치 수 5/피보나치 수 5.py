n = int(input())
test = []
count_one = 0
for i in range(0, n + 1):
    if i == 0:
        test.append(0)
    elif i == 1:
        test.append(1)
    else:
        test.append(test[i - 2] + test[i - 1])

print(test[n])

