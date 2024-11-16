# i와 k값을 혼동해서 씀,,
# dr, dl의 움직이는 값을 잘 못 씀,,
from collections import deque

dr = [0, 1, 0, -1]
dl = [1, 0, -1, 0]

T = int(input())

for t in range(1, T+1):
    n = int(input())
    
    lt = [[0 for _ in range(n)] for _ in range(n)]
    
    deq = deque([(0,0)])
    k = 1
    
    while deq:
        r, l = deq.pop()
        lt[r][l] = k
        k += 1
        
        for i in range(4):
            ddr = r + dr[i]
            ddl = l + dl[i]
            if 0 <= ddr < n and 0 <= ddl < n:
                if lt[ddr][ddl] == 0:
                    deq.append((ddr,ddl))
                    break
                
    print(f'#{t}')
    for row in lt:
        for n in row:
            print(n, end=" ")
        print("") 
            
    
    