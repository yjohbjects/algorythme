a, b = map(int, input().split(' '))

great = 0
least = 0

for i in range (min(a, b), 0, -1):
    if a % i == 0 and b % i == 0 :
        great = i
        break

for j in range(max(a, b), 10000000001, great):
    if j % a == 0 and j % b == 0:
        least = j
        break

print(great)
print(least)
