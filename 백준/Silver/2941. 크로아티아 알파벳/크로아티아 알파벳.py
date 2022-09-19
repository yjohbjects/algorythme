word = input()

word = word.replace('c=', '*')
word = word.replace('c-', '*')
word = word.replace('dz=', '*')
word = word.replace('d-', '*')
word = word.replace('lj', '*')
word = word.replace('nj', '*')
word = word.replace('s=', '*')
word = word.replace('z=', '*')

print(len(word))