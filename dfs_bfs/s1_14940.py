import sys
from collections import deque
input = sys.stdin.readline

def bfs(visited, n, m, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    deq = deque([(n,m)])
    
    while deq:
        q = deq.popleft()
        
        for i in range(4):
            yy = q[0] + dy[i]
            xx = q[1] + dx[i]
            if 0 <= yy < len(visited) and 0 <= xx < len(visited[0]):
                if graph[yy][xx] == 1 and visited[yy][xx] == 0:
                    visited[yy][xx] = visited[q[0]][q[1]] + 1
                    deq.append((yy, xx))
    return visited
    
n, m =  map(int, input().split())
graph = deque([])
visited = [[0 for _ in range(m)] for _ in range(n)]
sn, sm = 0, 0
for i in range(n):
    arr = list(map(int, input().strip().split()))
    if 2 in arr:
        sn = i
        sm = arr.index(2)
    graph.append(arr)

arr = bfs(visited, sn, sm, graph)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and arr[i][j] == 0:
            print(-1, end=" ")
        else:
            print(arr[i][j], end= " ")
    print()