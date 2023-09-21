A = input()
B = input()

score = {
    'A': 3, 
    'B': 2,
    'C': 1,
    'D': 2, 
    'E': 3, 
    'F': 3, 
    'G': 2, 
    'H': 3, 
    'I': 3, 
    'J': 2, 
    'K': 2, 
    'L': 1, 
    'M': 2, 
    'N': 2, 
    'O': 1, 
    'P': 2, 
    'Q': 2, 
    'R': 2, 
    'S': 1, 
    'T': 2, 
    'U': 1, 
    'V': 1, 
    'W': 1, 
    'X': 2, 
    'Y': 2, 
    'Z': 1 
}

calculate = []
is_hundred = False
for i in range(len(A)):
    calculate.append(score[A[i]])
    calculate.append(score[B[i]])

# print(calculate)
while len(calculate) != 2:
    temp = []
    for i in range(0, len(calculate)-1):
        temp.append((calculate[i] + calculate[i+1]) % 10)

    calculate = temp
    # print(calculate)

    if len(calculate) == 3:
        if str(calculate[0]) + str(calculate[1]) + str(calculate[2]) == '100':
            is_hundred = True

if is_hundred:
    print(100)

else:
    print((str(calculate[0]) + str(calculate[1])))