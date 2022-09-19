word = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = []
for char in alphabets:
    result.append(word.find(char))

print(*result)