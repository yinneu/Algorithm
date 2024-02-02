# 계수 정렬 (데이터 범위가 작은 (백만이내)에서 효과적인 정렬 시간 복잡도 O(N+K))
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000+1)

for _ in range(n):
    arr[int(input())] += 1 # cnt = [0] * (max(arr)+1) max값은 이미 주어졌으므로 바로 만들면 됨.
    
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)