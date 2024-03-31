# 절댓값 힙
import heapq
import sys
input = sys.stdin.readline

minus = []
plus = []

def printheap(n):
    result = 0
    if minus and plus:
        if minus[0] <= plus[0]:
            result = -(heapq.heappop(minus))
        else:
            result = heapq.heappop(plus)
    elif minus:
        result = -(heapq.heappop(minus))
    elif plus:
        result = heapq.heappop(plus)
    return result

N = int(input())
for _ in range(N):
    n = int(input())
    if n < 0:
        heapq.heappush(minus, -n)
    elif n > 0:
        heapq.heappush(plus, n)
    else:
        print(printheap(n))