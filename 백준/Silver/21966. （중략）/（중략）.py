N = int(input())
S = input()

if len(S) <= 25:
    print(S)

else:
    # print(S[11:len(S)-11].count('.'))
    if ('.' == S[11:len(S)-11][-1] and S[11:len(S)-11].count('.') == 1) or S[11:len(S)-11].count('.') == 0:
        print(S[:11] + '...' + S[len(S)-11:])
    else:
        print(S[:9] + '......' + S[len(S)-10:])
