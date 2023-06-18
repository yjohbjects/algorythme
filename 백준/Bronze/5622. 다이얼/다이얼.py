answer = 0

word = input()

for char in word:
    answer += 2

    if char in 'ABC':
        answer += 1
    
    elif char in 'DEF':
        answer += 2

    elif char in 'GHI':
        answer += 3

    elif char in 'JKL':
        answer += 4

    elif char in 'MNO':
        answer += 5

    elif char in 'PQRS':
        answer += 6

    elif char in 'TUV':
        answer += 7

    elif char in 'WXYZ':
        answer += 8

print(answer)