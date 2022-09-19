numbers = list(map(int, input().split()))

for i in range(len(numbers)-1, 0, -1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers[1])