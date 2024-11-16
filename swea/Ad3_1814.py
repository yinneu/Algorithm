#10개 중에 6개 맞음. 풀이중,,
from collections import deque

def dfs(v, cnt):
    global mxcnt

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt+1)

    # 더 이상 방문할 수 있는 점이 없다면, 방문처리를 취소해줌. (다른 경로를 위해)
    visited[v] = False #이게 포인트,,

    if cnt > mxcnt:
        mxcnt = cnt


T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append((n2))
        graph[n2].append((n1))

    mxcnt = 0
    cnt = 0

    for i in range(1, n+1):
        dfs(i,1)

    print(f'#{t} {mxcnt}')