N = int(input())
refrees = input()

a, b = 0, 0
for i in range(len(refrees)):
    if refrees[i] == 'A':
        a += 1
    else:
        b += 1

if a == b:
    print('Tie')

elif a > b:
    print('A')

elif a < b:
    print('B')