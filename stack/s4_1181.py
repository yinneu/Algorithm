from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    
    deq = deque()   
    arr = list(input().strip())
    
    for a in arr:
        if a == '(':
            deq.append(0)
        else:
            if deq:
                deq.pop()
            else:
                deq.append(0)
                break
            
    if deq:
        print("NO")
    else:
        print("YES")