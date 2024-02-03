# 기존 리스트 큐 사용시 시간 초과 됐던 문제
from collections import deque 

n = int(input())
deq = deque(range(1, n+1))

while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())

print(deq[0])