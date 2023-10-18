N = int(input())

student_id = []
for _ in range(N):
    student_id.append(input())

temp = ['' for _ in range(len(student_id))]
answer = 0
for i in range(len(student_id[0]) - 1, -1, -1):
    for j in range(len(student_id)):
        temp[j] = student_id[j][i] + temp[j]

    if len(set(temp)) == len(student_id):
        answer = len(temp[0])
        break
            
print(answer)    