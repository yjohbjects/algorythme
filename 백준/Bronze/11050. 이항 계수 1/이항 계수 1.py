def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

N, K = map(int, input().split())

print(factorial(N) // (factorial(K) * factorial(N - K)))