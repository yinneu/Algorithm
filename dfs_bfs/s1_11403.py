# 그래프 탐색 , 플로이드 - 워셜, 최단거리
from collections import deque
import copy
import sys
input = sys.stdin.readline

# 시작점이 다른 최단 거리를 생각하면 됨.
def bfs(visited, start, to):
    visited[start][to] = 1
    deq = deque([to])
    
    while deq:
        d = deq.popleft()
        
        for k in range(len(visited)):
            if visited[d][k] == 1 and visited[start][k] != 1:
                visited[start][k] = 1
                deq.append(k)
                
    return visited

N = int(input())
graph = []

for i in range(N):
    arr = list(map(int, input().strip().split()))
    graph.append(arr)
    
visited = copy.deepcopy(graph)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            visited = bfs(visited, i, j)
            
for row in visited:
    for col in row:
        print(col, end=' ')
    print()