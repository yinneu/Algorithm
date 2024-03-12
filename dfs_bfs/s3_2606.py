from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    cnt = 0
    visited[start] = True
    deq = deque([start])
    
    while deq:
        n = deq.popleft()
        for m in graph[n]:
            if not visited[m]:
                visited[m] = True
                deq.append(m)
                cnt += 1
    return cnt
                
n = int(input())
k = int(input())
com = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)
    
print(bfs(com, 1, visited))
    
