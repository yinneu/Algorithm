import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    visited = [-1] * len(graph)
    que = deque([start])
    visited[start] = 0
    
    while que:
        node = que.popleft()
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                que.append(i)
                
    return sum(visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

minN = n * n
check = -1
for i in range(n, 0, -1):
    total = bfs(graph, i)
    if total < minN and check == -1:
        minN = total
        check = i
print(check)



