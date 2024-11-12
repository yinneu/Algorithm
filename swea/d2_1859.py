# 17:24 소요, 짜면서 생각하지 말기,,
from collections import deque

T = int(input())

for t in range(1, T+1):
    n = int(input())
    ns = deque(map(int,input().split()))

    maxV = max(ns)

    cnt = 0
    money = 0
    while ns:
        nn = ns.popleft()
        #판매
        if nn == maxV:
            money += (nn * cnt)
            cnt = 0
            if ns:
                maxV = max(ns)
        #구매
        else:
            money -= nn
            cnt += 1

    result = 0
    if money > 0:
        result = money

    print(f'#{t} {result}')