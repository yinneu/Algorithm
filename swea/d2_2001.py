# 2001 파리퇴치
# f-string f'{변수명}'
# 왜인지 import sys 에서 컴파일 오류나서 그냥 빼고 씀
import sys
input = sys.stdin.readlines
from collections import deque

T = int(input())

for T in range(1, T+1):
    
    n, m = map(int, input().split())
    arr = deque()
    
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        
    maxSum = 0
    for i in range(m-1,n):
        for j in range(m-1,n):
            part = 0
            for k in range(0,m):
                for l in range(0,m):
                    part += arr[i-(m-1)+k][j-(m-1)+l]
            if part > maxSum:
                maxSum = part
                
    print(f'#{T} {maxSum}')