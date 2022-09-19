a = int(input())
b = int(input())
c = int(input())
num = a * b * c

result = [0 for _ in range(10)]
for char in str(num):
    if char == '1':
        result[1] += 1
    elif char == '2':
        result[2] += 1
    elif char == '3':
        result[3] += 1
    elif char == '4':
        result[4] += 1
    elif char == '5':
        result[5] += 1
    elif char == '6':
        result[6] += 1
    elif char == '7':
        result[7] += 1
    elif char == '8':
        result[8] += 1
    elif char == '9':
        result[9] += 1
    elif char == '0':
        result[0] += 1

print(*result, sep='\n')