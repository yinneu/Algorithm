T = int(input())

for tt in range(1,T+1):
    n, l = map(int, input().split())

    tk_lt = [(0,0)] # c 초기
    for _ in range(n):
        dt, dk = map(int, input().split())
        tk_lt.append((dt,dk))

    ll_lt = [[0 for _ in range(l+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        t, k = tk_lt[i]
        for j in range(1, l+1):
            if j < k:
                ll_lt[i][j] = ll_lt[i-1][j]
            else:
                ll_lt[i][j] = max(t + ll_lt[i-1][j-k],ll_lt[i-1][j])

    print(f'#{tt} {ll_lt[-1][-1]}')