import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

if n > 1:
    for i in range(2, len(dp)):
        if i % 6 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1 # 6의 배수인 경우 2로 나누어지는 경우도 고려해야한다.
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1
print(dp[n])