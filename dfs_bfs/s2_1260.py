from collections import deque
import sys
input = sys.stdin.readline

def DFS(graph, v, visited):   # 깊이 우선 탐색 (스택)
    visited[v] = True
    print(v, end=" ")
    graph[v].sort()         # 오름차순 조건
    for i in graph[v]: 
        if not visited[i]: # 방문하지 않은 정점
            DFS(graph, i, visited)
    
        
def BFS(graph, v, visited): # 너비 우선 탐색 (큐)
    dep = deque([v])
    visited[v] = True
    
    while dep:
        p = dep.popleft()
        print(p, end=" ")
        graph[p].sort()
        for i in graph[p]:
            if not visited[i]:
                dep.append(i)
                visited[i] = True

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visitedb = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    
    # 양방향
    graph[a].append(b)
    graph[b].append(a)
     
DFS(graph, v, visited)
print()
BFS(graph, v, visitedb)