from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, xy, visited):
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    deq = deque([(xy[0], xy[1])])
    visited[xy[0]][xy[1]] = True
    cnt = 0
    
    while deq:
        y, x = deq.popleft()        
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < len(graph) and 0 <= xx < len(graph[0]):
                if not visited[yy][xx] and graph[yy][xx] != 'X':
                    visited[yy][xx] = True
                    deq.append((yy, xx))
                    if graph[yy][xx] == 'P':
                        cnt += 1
    return cnt 

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
graph = deque([])
iloc = [-1, -1]
for i in range(n):
    row = input().strip()
    if iloc[0] == -1:
        for j in range(m):
            if row[j] == 'I':
                iloc[0] = i
                iloc[1] = j
                break
    graph.append(row)
    
result = bfs(graph, iloc, visited)
if  result > 0:
    print(result)
else:
    print('TT')