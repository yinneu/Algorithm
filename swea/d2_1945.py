lt = [2, 3, 5, 7, 11]

T = int(input())

for t in range(1, T+1):
    cnt = {2:0, 3:0, 5:0, 7:0, 11:0}

    N = int(input())

    for i in lt:
        while N % i == 0:
            N //= i
            cnt[i] += 1

    print(f'#{t}', end=" ")
    for i in lt:
        print(cnt[i], end = " ")
    print("")