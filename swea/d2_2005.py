T = int(input())

for t in range(1, T+1):
    N = int(input())

    lt = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for l in range(r+1):
            if l == 0 or l == r:
                lt[r][l] = 1
            else:
                lt[r][l] = lt[r-1][l-1] + lt[r-1][l]

    print(f'#{t}')
    for r in lt:
        for l in r:
            if l != 0:
                print(l, end=" ")
        print("")