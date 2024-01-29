import sys
input = sys.stdin.readline

mt = [list(range(1, 15))]

def dp(k, n):
    for i in range(1, k+1):
        mt.append([1] * 14)
        for j in range(1, n):
            mt[i][j] = mt[i-1][j] + mt[i][j-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    
    dp(k, n)
    print(mt[k][n-1])