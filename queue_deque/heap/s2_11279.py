# 최대힙 (우선순위큐)
import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)