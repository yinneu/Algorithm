T = int(input())

for t in range(1, T+1):
    lt = list(map(int, input().split()))

    lt.remove(max(lt))
    lt.remove(min(lt))

    total = sum(lt)
    div = total / len(lt)

    print(f'#{t} {round(div)}')