N = int(input())

sad = 0
happy = 0

nums = list(map(int, input().split()))
for num in nums:
    if num % 2 == 0:
        happy += 1
    else:
        sad += 1

if sad >= happy:
    print('Sad')
else:
    print('Happy')