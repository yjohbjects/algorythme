T = int(input())
for _ in range(T):
    pw = input()
    if 6 <= len(pw) <= 9:
        print('yes')
    else:
        print('no')