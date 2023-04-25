N = int(input())

decrypt = 'abcdefghijklmnopqrstuvwxyz'
encrypt = 'wghuvijxpqrstacdebfklmnoyz'

decryption = {}
for i in range(len(decrypt)):
    decryption[encrypt[i]] = decrypt[i]

for _ in range(N):
    encrypted = input()
    encrypted = encrypted.replace(' ', '')
    temp = {}

    for letter in encrypted:
        if letter in temp:
            temp[letter] += 1
        else:
            temp[letter] = 1


    answer = [k for k, v in temp.items() if v == max(list(temp.values()))]

    print('?' if len(answer) > 1 else answer[0])

