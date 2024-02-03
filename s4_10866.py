from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
n = int(input())

for _ in range(n):
    arr = input().strip().split()
    
    if len(arr) > 1:
        if arr[0] == 'push_front':
            deq.appendleft(int(arr[1]))
        else:
            deq.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif arr[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(deq))
    elif arr[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)