N = int(input())
nums = sorted(list(map(int, input().split())))

M = int(input())
search = list(map(int, input().split()))

for num in search:
    left = 0
    right = len(nums) - 1


    while abs(left - right) > 1:
        pin = (left + right) // 2

        if nums[pin] == num or nums[left] == num or nums[right] == num:
            print(1)
            break
        else:
            if num > nums[pin]:
                left = pin
            else:
                right = pin

    else: 
        print(0)