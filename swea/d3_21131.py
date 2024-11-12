# 53:16, 전치행렬을 만드는 과정이나 for문에서 (start,end) 값을 잘못 설정함.
# 주요 로직 먼저 짜기,,
def transpose(lt, x):
    xx = x+1
    check = [[False for _ in range(xx)] for _ in range(xx)]

    for i in range(0,xx):
        for j in range(0,xx):
            if not check[j][i] and i != j:
                check[i][j] = True
                temp = lt[i][j]
                lt[i][j] = lt[j][i]
                lt[j][i] = temp
                #swap: lt[i][j], lt[j][i] = lt[j][i], lt[i][j]
    return lt

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lt = []

    for i in range(N):
        row = list(map(int, input().split()))
        lt.append(row)

    cnt = 0
    for i in range(N-1,-1, -1):
        #체크
        for j in range(N-1, -1, -1):
            do = i * N + (j+1)
            if lt[i][j] != do:
                #뒤집기고 다음으로
                lt = transpose(lt, i)
                cnt += 1
                break

    print(cnt)
