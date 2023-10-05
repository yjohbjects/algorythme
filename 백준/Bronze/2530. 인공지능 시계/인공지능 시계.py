A, B, C = map(int, input().split())
addup = int(input())

A += addup // 3600
addup -= (addup // 3600) * 3600

B += addup // 60
addup -= (addup // 60) * 60

C += addup

if C >= 60:
    B += C // 60
    C -= (C // 60) * 60

if B >= 60:
    A += B // 60
    B -= (B // 60) * 60

if A >= 24:
    A -= (A // 24) * 24
print(A, B, C)