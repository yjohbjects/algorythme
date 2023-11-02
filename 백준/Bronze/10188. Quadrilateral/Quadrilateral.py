for _ in range(int(input())) :
    length, width = map(int, input().split())
    for _ in range(width) :
        print('X' * length)
    print()