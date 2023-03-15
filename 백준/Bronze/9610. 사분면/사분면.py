N = int(input())
answer = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}

for _ in range(N):
    x, y = input().split(' ')

    if x == '0' or y == '0':
        answer['AXIS'] += 1

    elif x[0] != '-':
         if y[0] != '-' :
              answer['Q1'] += 1 
         else:
              answer['Q4'] += 1

    elif x[0] == '-':
        if y[0] != '-':
             answer['Q2'] += 1
        else:
             answer['Q3'] += 1

# print(answer)
for item in answer:
     print(f"{item}: {answer[item]}")