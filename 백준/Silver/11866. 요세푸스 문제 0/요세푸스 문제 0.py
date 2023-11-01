from collections import deque

N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
answer = []

counter = 0
idx = 0
while len(nums) != len(answer):
    idx = idx % N
    
    if nums[idx] != 0:
        counter += 1

        if counter == K:
            answer.append(nums[idx])
            nums[idx] = 0
            counter = 0
    idx += 1

ans = '<'
for n in answer:
    ans += str(n) + ', '

temp = ', '.join(map(str, answer))
print(f'<{temp}>')