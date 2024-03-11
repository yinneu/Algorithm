# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, check):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    arr[0][0] = 1
    deq = deque([(0,0)])

    while deq:
        i, j = deq.popleft()
        for k in range(4):           
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < n and 0 <= x < m and check[y][x] == '1':        
                if arr[y][x] == -1:
                    arr[y][x] = arr[i][j] + 1
                    deq.append((y,x))
    return arr[-1][-1]
    
n, m = map(int, input().split())
arr = [[-1 for _ in range(m)] for _ in range(n)]
check = []
for _ in range(n):
    nums = input().strip()
    check.append(nums)
                    
print(bfs(arr, check))