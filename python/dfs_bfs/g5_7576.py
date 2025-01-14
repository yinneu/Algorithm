#bfs #토마토
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, check):
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    deq = check
    maxday = 1
    
    while deq:
        t = deq.popleft()
        
        for d in range(4):
            yy = t[0] + dy[d]
            xx = t[1] + dx[d]
            if 0 <= yy < len(graph) and 0 <= xx < len(graph[0]):
                if graph[yy][xx] == 0:
                    days = graph[t[0]][t[1]] + 1
                    graph[yy][xx] = days
                    deq.append((yy, xx))
                    if days > maxday:
                        maxday = days
    for low in graph:
        if 0 in low:
            return -1
        
    return maxday-1

graph = []
check = deque([])
flag = False

m, n = map(int, input().split())
for i in range(n):
    arr = list(map(int, input().strip().split()))
    graph.append(arr)
    for j in range(m):
        if not flag and arr[j] == 0:
            flag = True
        elif arr[j] == 1:
            check.append((i, j))
            
if flag:
    print(bfs(graph, check))
else:
    print(0)