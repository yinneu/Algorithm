T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):
    date = input()
    y = date[:4]
    m = date[4:6]
    d = date[6:]

    if 0 < int(m) < 13 and 0 < int(d) <= days[int(m)]:
        result = f'{y}/{m}/{d}'
    else:
        result = -1

    print(f'#{t} {result}')