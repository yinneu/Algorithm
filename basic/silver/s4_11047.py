import sys
input =sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    m = int(input())    
    if m <= k:
        arr.append(m)

cnt = 0
for i in range(len(arr)-1, -1, -1):
    if k == 0:
        break
    cnt += (k // arr[i])
    k %= arr[i]
    
print(cnt)