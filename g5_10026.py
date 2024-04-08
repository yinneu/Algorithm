from collections import deque
import sys
input = sys.stdin.readline

def bfs(visited, i, j, check): # check 색약 여부
    
    dn = [0, 0, -1, 1]
    dm = [-1, 1, 0, 0]
    
    deq = deque([(i,j)])
    visited[i][j] = True
    
    if check:
        lt = ['R', 'G']
    else:
        lt = [graph[i][j]]
    
    while deq:
        n,m = deq.popleft()
        for i in range(4):
            nn = n + dn[i]
            mm = m + dm[i]
            if 0 <= nn < N and 0 <= mm < N:
                if graph[nn][mm] in lt and not visited[nn][mm]:
                    visited[nn][mm] = True
                    deq.append((nn,mm))


N = int(input())

graph = []
result = [0, 0]
visitedA = [[False for _ in range(N)] for _ in range(N)] # 색약이 아닌 사람
visitedB = [[False for _ in range(N)] for _ in range(N)] # 색약인 사람

for _ in range(N):
    graph.append(input().strip())

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'B':
            if not visitedA[i][j]:
                bfs(visitedA, i, j, False)
                result[0] += 1
                result[1] += 1
        else:      
            if not visitedA[i][j]:
                bfs(visitedA, i, j, False)
                result[0] += 1
            if not visitedB[i][j]:
                bfs(visitedB, i, j, True)
                result[1] += 1
print(*result)