price, num, budget = map(int, input().split(' '))

if price * num > budget:
    print((price * num) - budget)

else:
    print(0)