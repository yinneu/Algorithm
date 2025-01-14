# 타일링 경우의 수 # dp,,?
import sys
import math
input = sys.stdin.readline

n = int(input())
        
 # 자리 배치
result = 1 # 모두 1 x 2 타일인 경우

# 2 x 1 개수에 따른 배치
for i in range(1, (n//2)+1): # 1개일 때, 
    m = n-i # 전체 개수 - 가로 쌍의 개수 = 전체 자리 수
    num = math.comb(m,i) # 가로 쌍 자리 뽑기
    result += (num)
    
result %= 10007
print(result)