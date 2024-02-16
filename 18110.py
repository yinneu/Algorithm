import sys # 13%에서 틀림,,,
input = sys.stdin.readline

arr = [0] * 31
n = int(input())

for _ in range(n):
    arr[int(input())] += 1
    
m = round(n * 0.15)
m2 = n - ( m * 2 )
m3 = m2
sumN = 0

for i in range(1, 31):
    if arr[i] != 0:    # 카운트 값이 있고
        if m != 0:
            if arr[i] < m:    
                m -= arr[i]
            else:        # arr[i] >= m
                arr[i] -= m
                m = 0
                       
        if m == 0 and arr[i] > 0:
            if arr[i] <= m2:
                sumN += (i * arr[i])
                m2 -= arr[i]
            else:
                sumN += (i * m2)
                break

if n != 0:
    print(round(sumN/m3))   
else:
    print(0)