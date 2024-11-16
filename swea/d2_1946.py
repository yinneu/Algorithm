#출력 시 줄 바뀜 조심.
T = int(input())

for t in range(1, T+1):
    n = int(input())

    lt = []
    for i in range(n):
        s, n = input().split()
        lt.append((s,int(n)))

    cnt = 0
    print(f'#{t}')
    for i in lt:
        for j in range(i[1]):
            print(i[0], end="")
            cnt += 1
            if cnt == 10:
                print("")
                cnt = 0
    print("")