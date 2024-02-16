#1. 부동소수점 이해
#2. round 오사오입 -> 사사오입, int(N +0.5) 방식을 사용하거나 별도의 함수를 구현
# m을 구하는 부분이 아닌 
import sys
input = sys.stdin.readline

arr = [0] * 31
n = int(input())

for _ in range(n):
    arr[int(input())] += 1
    
m = int(n * 0.15 + 0.5)
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
    print(int(sumN/m3 + 0.5))   
else:
    print(0)