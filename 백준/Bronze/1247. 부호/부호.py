for _ in range(3):
    T = int(input())

    temp = 0
    for _ in range(T):
        temp += int(input())

    if temp == 0:
        print(0)

    elif temp > 0:
        print('+')
    
    else:
        print('-')

