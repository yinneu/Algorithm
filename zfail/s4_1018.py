import sys
input = sys.stdin.readline

a, b = map(int, input().split())
check = [[0 for _ in range(b)] for _ in range(a)]

arr = []
for _ in range(a):
    arr.append(list(input().strip()))
    
minN = 64   
for n in range(0, a-7):
    for m in range(0, b-7):
        one = arr[n][m]
        two = 'B' if one == 'W' else 'W'        
        cnt = 0
        for i in range(n, n+8):
                if i != 0 or i % 2 != 0:
                    one, two = two, one

                for j in range(m, m+8):
                    if j == 0 or j % 2 == 0:
                        if arr[i][j] != one:
                            cnt += 1
                    else:
                        if arr[i][j] != two:
                            cnt += 1
        if cnt < minN:
            minN = cnt


print(minN)
        
    
    
# check = [[0] * b ] * a : 리스트 값 변경시 특정 열이 아닌 모든 열이 적용 됨..