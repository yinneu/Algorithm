# 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().strip().split()))
cnt = [0] * (n + 1)

s = 0
for i in range(0, n):
    cnt[i+1] = cnt[i] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(cnt[b]-cnt[a-1])