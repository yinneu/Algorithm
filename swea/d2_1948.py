day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T+1):
    sm, sd, dm, dd = map(int, input().split())

    if sm == dm:
        result = dd - sd + 1
    else:
        result = day[sm] - sd + 1
        for i in range(sm+1, dm):
            result += day[i]
        result += dd

    print(f'#{t} {result}')
