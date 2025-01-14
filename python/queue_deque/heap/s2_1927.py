import sys
import heapq
input = sys.stdin.readline

heap = []
t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 0:
        if heap:
            print(heapq.heappop(heap)) 
        else:
            print(0)
    else:
        heapq.heappush(heap,n)