# 제한시간 초과 -> 규칙찾기
T = int(input())

for t in range(1, T+1):
    n = int(input())
    
    s2 = n * n
    s3 = n * n + n
    s1 = s3 // 2
            
    print(f'#{t} {s1} {s2} {s3}')
    