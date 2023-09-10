N = int(input())

label = '-WelcomeToSMUPC'

if N % 14 == 0:
    print('C')
else:
    print(label[N % 14])