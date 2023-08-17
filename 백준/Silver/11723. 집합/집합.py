import sys

M = int(sys.stdin.readline())

S = set()

for _ in range(M):

    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == 'all':
            S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

        elif command[0] == 'empty':
            S.clear()

    else:
        number = int(command[1])
        
        if command[0] == 'add':
            S.add(number)

        elif command[0] == 'remove':
            S.discard(number)

        elif command[0] == 'check':
            if number in S:
                sys.stdout.write(str(1) + '\n')
            else:
                sys.stdout.write(str(0) + '\n')
            
        elif command[0] == 'toggle':
            if number in S:
                S.discard(number)
            else:
                S.add(number)
