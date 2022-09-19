word = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = [0] * 26

for char in word:
    result[(alphabets.find(char))] += 1

print(*result)