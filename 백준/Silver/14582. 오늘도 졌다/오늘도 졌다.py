W = list(map(int, input().split()))
S = list(map(int, input().split()))

yes = False
w, s = 0, 0
for i in range(9):
    w += W[i]
    if w > s:
        yes = True
        
    s += S[i]

    if w > s:
        yes = True

print('Yes' if yes else 'No')