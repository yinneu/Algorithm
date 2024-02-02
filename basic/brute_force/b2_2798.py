# https://www.acmicpc.net/problem/2798
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxN = 0

for i in range(0,n):
    for j in range(i+1, n):
        if arr[i] + arr[j] < m :
            for k in range(j+1,n):
                temp = arr[i] + arr[j] + arr[k]
                if temp <= m and maxN < temp:
                    maxN = temp
                    
print(maxN)

## 생각보다 숫자의 개수가 크지 않아서 for문으로 풀어도 괜찮은 것 같음.