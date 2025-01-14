T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    
    H = n % h
    if H == 0:
        H = h
        W = n // h
    else:
        W = n // h + 1
    R = (H * 100) + W
    
    print(R)
    
    # 나눗셈 계산이 있을 때는 딱 나누어 떨어진 경우도 고려해야한다.