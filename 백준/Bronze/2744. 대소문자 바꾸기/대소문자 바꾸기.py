# B2744 대소문자바꾸기

word = input()

result = ''
for char in word:
    if char.isupper():
        result += char.lower()

    else:
        result += char.upper()

print(result)