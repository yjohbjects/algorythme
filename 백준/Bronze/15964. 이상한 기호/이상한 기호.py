# A＠B = (A+B)×(A-B)

def calculator(a, b):
    return (a+b) * (a-b)

A, B = map(int, input().split())
print(calculator(A, B))