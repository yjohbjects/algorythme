lib = input()
word = input()

while word in lib:
    lib = lib.replace(word, '@')

print(lib.count('@'))