# dp, python3로 돌리면 시간초과, pypy3로 돌면 통과,,
# 조합이 1개, 2개, 3개, 4개인 경우의 조건을 나누어서 해야 불필요한 반복을 제외할 수 있다.
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

i = 1
while i*i <= n:
    dp[i*i] = 1 # 기저사례
    i += 1

for j in range(1, n+1):
    if dp[j] == 1:
        continue
    k = 1
    while k*k <= j:
        if dp[j] == 0:
            dp[j] = dp[k*k] + dp[j - (k*k)]
        else:
            dp[j] = min(dp[j], dp[k*k] + dp[j - (k*k)]) # 여기서 너무 많이 도는 것 같음.
        k += 1
        
print(dp[n])

