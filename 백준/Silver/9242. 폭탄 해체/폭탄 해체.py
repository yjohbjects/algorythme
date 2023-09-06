bomb = []
for _ in range(5):
    bomb.append(input())

'''
***   * *** *** * * *** *** *** *** ***
* *   *   *   * * * *   *     * * * * *
* *   * *** *** *** *** ***   * *** ***
* *   * *     *   *   * * *   * * *   *
***   * *** ***   * *** ***   * *** ***
'''

isValid = True
password = ''
# len(bomb[1]) // 4 + 1 => 암호의 길이
for i in range(len(bomb[1]) // 4 + 1):
    number = bomb[0][i*4:i*4+3] + bomb[1][i*4:i*4+3] + bomb[2][i*4:i*4+3] + bomb[3][i*4:i*4+3] + bomb[4][i*4:i*4+3]

    if number == '**** ** ** ****':
        password += '0'
    elif number == '  *  *  *  *  *':
        password += '1'
    elif number == '***  *****  ***':
        password += '2'
    elif number == '***  ****  ****':
        password += '3'
    elif number == '* ** ****  *  *':
        password += '4'
    elif number == '****  ***  ****':
        password += '5'
    elif number == '****  **** ****':
        password += '6'
    elif number == '***  *  *  *  *':
        password += '7'
    elif number == '**** ***** ****':
        password += '8'
    elif number == '**** ****  ****':
        password += '9'
    else:
        isValid = False

if isValid and int(password) % 6 == 0:
    print('BEER!!')
else:
    print('BOOM!!')

