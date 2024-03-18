# 타일링 경우의 수
import sys
from itertools import *
input = sys.stdin.readline

n = int(input())
m = n // 2
result = 0
if n % 2 == 0:
    result = (2 ** m) % 10007
else:
    # fac = [0] * (m + 1)
    # fac[1] = 1
    # for i in range(2, m+1):
    #     fac[i] = fac[i-1] * i
        
    dataset = [i for i in range(1, m+1)]
    print(dataset)
    result = 1
    for j in range(1, m+1):
        #c = fac[m] // (fac[j] * (fac[m]-fac[j]))
        # c = (fac[m]-fac[j]) 
        # 조합의 수
        num = len(list(combinations(dataset, j))) #j개를 가로로 배열한 경우
        print('nums: ', num, '-> ', (num * (j+1)))
        result += (num * (j+1))
        print(result)
        
    result %= 10007
        
print(result)
        
    
    
    