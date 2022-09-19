T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())

    print(f'#{t} {((N//P)**(P-(N%P))) * (N//P+1)**(N%P)}')