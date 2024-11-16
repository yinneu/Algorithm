#dp : 보류 너무 어렵다,,

# 부피의 합이 ~ 것 중에 가장 큰 것?
from collections import deque

T = int(input())

for t in range(1, T+1):
    n, k = map(int,input().split())
    
    vc_lt = deque([[] for _ in range(k+1)])
    dp = deque([0] for _ in range(k+1))
    
    for _ in range(n):
        v, c = map(int,input().split())
        vc_lt[v].append(c)
        
    for r in vc_lt:
        r.sort(resverse=True)
        
    dp[1] = vc_lt[1][-1]
    for i in range(2, k):
        if i == 2:
            if lt[i][0] > dp[i] + lt[1]:
                dp[i] = lt[i][1]
        
        
        
        
    
        
    