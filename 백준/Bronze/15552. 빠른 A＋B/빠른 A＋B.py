import sys
T = int(input())
for t in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)