# 재귀함수를 통한 dfs 구현 -> RecursionError
# 스택/큐를 활용한 dfs 구현

#import sys
#input = sys.stdin.readline

# 섬 카운트
# 방문 확인 리스트
# (0,0)



from collections import deque

def dfs_deque(graph, start, visited):

    dx = [0, 0, -1, 1, -1, -1, 1, 1] #행
    dy = [-1, 1, 0, 0, 1, -1, 1, -1] #열
    check_deque = deque()

    check_deque.append(start)

    #8가지 방향을 모두 탐색 1. 범위 안, 2. 방문하지 않음 3. 섬이여야함.
    while check_deque:
        node = check_deque.pop()

        for i in range(8):
            yy = node[0] + dy[i]
            xx = node[1] + dx[i]
            if 0 <= xx < len(graph[0]) and 0 <= yy < len(graph):
                if not visited[yy][xx] and graph[yy][xx] == 1:
                    visited[yy][xx] = True
                    check_deque.append((yy,xx))

    return 1


def get_island(w, h):
    island = 0 # 섬 개수
    graph = []
    visited = [[False for _ in range(w)] for _ in range(h)]

    #그래프 받기
    for i in range(h):
        row = list(map(int, input().split()))
        graph.append(row)

    # 섬 개수 구하기
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                island += dfs_deque(graph, (i,j), visited)
    
    return island


while(True):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        print(get_island(w,h))