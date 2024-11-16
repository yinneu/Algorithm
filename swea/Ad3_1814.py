#10개 중에 6개 맞음. 풀이중,,
from collections import deque

def dfs(graph, start):
    check = [[-1 for _ in range(len(graph))] for _ in range(len(graph))]

    deq = deque()
    deq.append(start)
    check[start][start] = 1
    # [n][n]는 데이터 기록하고, [n][m] 방문기록.
    while deq:
        node = deq.pop()
        for n in graph[node]:
            if check[node][n] == -1: #이 경로로 방문하지 않은 경우
                if check[n][n] < check[node][node] + 1:
                    check[n][n] = check[node][node] + 1
                    deq.append(n)
                check[node][n] = 0 #무방향 그래프니까 체크해줘야함.
                check[n][node] = 0

    max_v = max(map(max, check))

    return max_v


T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        n1, n2 = map(int, input().split())

        graph[n1].append((n2))
        graph[n2].append((n1))

    mxcnt = 0

    for i in range(1, n+1):
        cnt = dfs(graph, i)
        if cnt > mxcnt:
            mxcnt = cnt

    print(f'#{t} {mxcnt}')