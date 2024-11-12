#11:26
T = int(input())

for t in range(1, T+1):
    a, b, n = map(int,input().split())

    x = a
    y = b
    cnt = 0

    while x <= n and y <= n:
        if x > y:
            y += x
        else:
            x += y
        cnt += 1

    print(cnt)