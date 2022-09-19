numbers = []
for _ in range(9):
    numbers.append(int(input()))

maxV = 0
maxV_index = 99
for i in range(len(numbers)):
    if numbers[i] > maxV:
        maxV = numbers[i]
        maxV_index = i+1

print(maxV)
print(maxV_index)