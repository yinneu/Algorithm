from collections import deque
import sys
input = sys.stdin.readline

def bfs(visited, n, m, graph):
    
    dn = [0, 0, 1, -1]
    dm = [1, -1, 0, 0]
    
    deq = deque([(n, m)])
    visited[n][m] = True
    cnt = 1
    
    while deq:
        tn, tm = deq.popleft()
        
        for i in range(4):
            nn = tn + dn[i]
            mm = tm + dm[i]
            if 0 <= nn < len(graph) and 0 <= mm < len(graph[0]):
                if not visited[nn][mm] and graph[nn][mm] == '1':
                    visited[nn][mm] = True
                    cnt += 1
                    deq.append((nn,mm))                 
    return cnt

N = int(input())
graph = []
visited = [[False for _ in range(N)] for _ in range(N)]
result = []

for _ in range(N):
    graph.append(input().strip())
    
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '1':
            result.append(bfs(visited, i, j, graph))

result.sort()
print(len(result))
for r in result:
    print(r)