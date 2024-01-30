a, b, v = map(int, input().split())

t1 = v - a
t2 = a - b

if t1 == 0 :
    print(1)
else:
    if t1 % t2 != 0:
        print(t1 // t2 + 2)
    else:
        print(t1 // t2 + 1)
        
## 목적지에 도달하는 순간은 a > b 보다 항상 크므로 낮에 도착할 수 밖에 없다.
# 전체 거리에서 낮에 이동하는 거리를 제외하고 하루 동안 움직이는 거리로 나누어 계산하였다.
# *** 조건을 잘 볼 것!