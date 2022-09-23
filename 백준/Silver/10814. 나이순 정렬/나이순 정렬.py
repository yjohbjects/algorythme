# B10814 나이순 정렬

N = int(input())

accounts = []
for i in range(N):
    age, name = map(str, input().split())
    accounts.append([int(age), name])

# accounts = sorted(accounts, key=lambda x:x[1], reverse=True)
accounts = sorted(accounts, key=lambda x:x[0])

for i in range(N):
    print(*accounts[i])
# print(*accunts)
