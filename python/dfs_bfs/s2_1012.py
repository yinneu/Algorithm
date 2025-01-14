# bfs
import sys
from collections import deque
input = sys.stdin.readline

# visited 와 graph 배열 두 개를 생성하여 체크할 수도 있음.
# 상하좌우를 확인하는 경우, dx = [0, 0, -1, 1], dy = [1,-1, 0, 0]를 for 문으로 조합하는 방식을 많이 사용함.

def bfs(check, arr):
    cnt = 0
    while check:
        deq = deque([check.pop()])
        cnt += 1
        
        while deq:  # 인접한 배추 체크
            n = deq.popleft()
            y = n[0]
            x = n[1]

            if (y+1, x) in check:
                    check.remove((y+1, x))
                    deq.append((y+1,x))
            if (y-1, x) in check:
                    check.remove((y-1, x))
                    deq.append((y-1,x))
            if (y, x+1) in check:
                    check.remove((y, x+1))
                    deq.append((y,x+1))
            if (y, x-1) in check:
                    check.remove((y, x-1))
                    deq.append((y,x-1))
    return cnt
    
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    
    arr = [[0 for _ in range(m)] for _ in range(n)]
    check = set()
    
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] += 1
        check.add((y,x))
    
    print(bfs(check,arr))