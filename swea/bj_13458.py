# import math, math.ceil: 실수 입력 시 올림, math.floor: 실수 입력시 내림
n = int(input())
ai = list(map(int, input().split()))
s1, s2 = map(int, input().split())

total = n

for i in ai:
    m = i - s1 #총감독관 감시
    if m > 0:
        d1 = m // s2
        d2 = m % s2
        if d2 == 0:
            total += d1
        else:
            total += (d1+1)

print(total)
