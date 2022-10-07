for t in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))

    dump = 0
    while dump < N:
        minV = 101
        min_idx = 101
        maxV = 0
        max_idx = 101
        for i in range(100):
            if nums[i] > maxV:
                maxV = nums[i]
                max_idx = i

            if nums[i] < minV:
                minV = nums[i]
                min_idx = i

        nums[max_idx] -= 1
        nums[min_idx] += 1
        dump += 1

    print(f'#{t} {max(nums) - min(nums)}')