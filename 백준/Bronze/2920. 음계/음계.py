# B2920 음계

doremi = list(map(int, input().split()))

descending = sorted(doremi, reverse=True)
ascending = sorted(doremi)

if doremi == descending:
    print('descending')

elif doremi == ascending:
    print('ascending')

else:
    print('mixed')