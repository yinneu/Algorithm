#v값을 중심으로 풀어야하는 것을 알야함.
#dp
T = int(input())

for t in range(1,T+1):
    n, k = map(int, input().split())

    vc_lt = [(0,0)]
    for i in range(n):
        v, c = map(int, input().split())
        vc_lt.append((v,c))

    kk_lt = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        v, c = vc_lt[i]
        for j in range(1, k+1):
            if j < v:
                kk_lt[i][j] = kk_lt[i-1][j]
            else:
                kk_lt[i][j] = max(c + kk_lt[i-1][j-v], kk_lt[i-1][j])

    print(f'#{t} {kk_lt[-1][-1]}')