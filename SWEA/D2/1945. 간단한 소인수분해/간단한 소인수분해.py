T = int(input())
for t in range(1, T + 1):
    num = int(input())

    two = 0
    while num % 2 == 0:
        num = num // 2
        two += 1

    three = 0
    while num % 3 == 0:
        num = num // 3
        three += 1

    five = 0
    while num % 5 == 0:
        num = num // 5
        five += 1

    seven = 0
    while num % 7 == 0:
        num = num // 7
        seven += 1

    eleven = 0
    while num % 11 == 0:
        num = num // 11
        eleven += 1

    print(f'#{t} {two} {three} {five} {seven} {eleven}')