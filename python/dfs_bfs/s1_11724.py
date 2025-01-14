# 연결 요소 갯수 구하기 (dfs가 더 적합한 듯하다.)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    deq = deque([start])
    visited[start] = True
    
    while deq:
        node = deq.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
        
print(cnt)