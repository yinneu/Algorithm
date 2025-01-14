# 숨바꼭질 #bfs #오답쓰기
# 참고 https://www.acmicpc.net/board/view/136673
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k, visited):
    deq = deque([n])
    visited[n] = 0
    
    while deq:
        nn = deq.popleft()
        
        for m in [nn-1, nn+1, nn*2]:
            if m == k:
                visited[m] = visited[nn] + 1
                return visited[m]
            if 0 <= m < len(visited) and visited[m] == -1:
                deq.append(m)
                visited[m] = visited[nn] + 1  
            
    return visited[k]

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    visited = [-1] * 100001
    print(bfs(n,k,visited))