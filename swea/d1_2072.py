T = int(input())

for t in range(1,T+1):
    arr = list(map(int,input().split()))

    total = 0

    for a in arr:
        if a % 2 == 1:
            total += a
    
    print(f'#{t} {total}')