N = int(input())
subjects = {}
for _ in range(N):
    a, b = input().split()
    subjects[a] = b

num = list(subjects.values()).index(min(subjects.values()))
print(list(subjects.keys())[num])