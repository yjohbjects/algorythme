A, B, C = map(int, input().split())

one = 0
two = 0

if A == 1:
    one += 1
    
if B == 1:
    one += 1
    
if C == 1:
    one += 1
    
if one > 3 - one:
    print(1)
    
else:
    print(2)