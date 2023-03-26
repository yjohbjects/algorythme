N = int(input())

A, B = 100, 100
for _ in range(N):
    a, b = map(int, input().split(' '))
    if a > b:
        B -= a
    elif a < b:
        A -= b

print(A)
print(B)
