# dp, 계단오르기
import sys
input = sys.stdin.readline

def dp(n, arr):
    if n == 1:
        return arr[1]
    if n == 2:
        return arr[1] + arr[2]
    ss = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n):
        if i < 2:
            ss[i][i+1] = ss[0][i] + arr[i+1]
            ss[i][i+2] = ss[0][i] + arr[i+2]
        elif i == (n-1):
            ss[i][i+1] = ss[i-2][i] + arr[i+1]
        else:
            ss[i][i+1] = ss[i-2][i] + arr[i+1]
            ss[i][i+2] = max(ss[i-2][i],ss[i-1][i]) + arr[i+2]
            
    return max(ss[n-2][n],ss[n-1][n])           

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
print(dp(n, arr))