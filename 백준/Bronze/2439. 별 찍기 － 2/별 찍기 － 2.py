# B2439 별 찍기 - 2

num = int(input())
for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * i)
