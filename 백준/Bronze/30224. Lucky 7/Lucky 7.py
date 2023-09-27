N = int(input())

does_contain = True if '7' in str(N) else False

if not does_contain and N % 7 == 0:
    print(1)
elif not does_contain and N % 7 != 0:
    print(0)
elif does_contain and N % 7 == 0:
    print(3)
else:
    print(2)