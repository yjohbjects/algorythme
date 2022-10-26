burger_min = 2001
drink_min = 2001

for _ in range(3):
    burger = int(input())

    if burger < burger_min:
        burger_min = burger


for _ in range(2):
    drink = int(input())

    if drink < drink_min:
        drink_min = drink

print(burger_min + drink_min - 50)