from collections import deque
import sys
input = sys.stdin.readline

graph = deque([])
check = deque([])

def indata(m, n, h):
    for i in range(h):
        arr = []
        for j in range(n):
            arr.append(list(map(int, input().strip().split())))
            for k in range(m):
                if arr[j][k] == 1:
                    check.append((i, j, k))
        graph.append(arr)
 
def bfs(visited, m, n, h):
    count = 0
    dh = [0, 0, 0, 0, -1, 1]
    dn = [-1, 1, 0, 0, 0, 0]  
    dm = [0, 0, -1, 1, 0, 0]   

    while check:
        th, tn, tm = check.popleft()
        for i in range(6):
            hh = th + dh[i]
            nn = tn + dn[i]
            mm = tm + dm[i]
            if  0 <= hh < h and 0 <= nn < n and 0 <= mm < m:
                if graph[hh][nn][mm] == 0 and visited[hh][nn][mm] == 0:
                    visited[hh][nn][mm] = visited[th][tn][tm] + 1
                    check.append((hh, nn, mm))
                    if count < visited[hh][nn][mm]:
                        count = visited[hh][nn][mm]
                        
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == 0 and graph[i][j][k] == 0:
                    return -1
    return count    
    
if __name__ == '__main__':
    m, n, h = map(int, input().split())
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    
    indata(m, n, h)

    print(bfs(visited, m, n, h))
