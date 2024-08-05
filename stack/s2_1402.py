# cursor를 int로 저장하는 방식을 사용하다가 시간초과 남.
# stack 방식을 사용해서 cursor를 기준으로 오른쪽 단어와 왼쪽 단어를 나눔

import sys
from collections import deque 
input = sys.stdin.readline

left = deque(input().strip())
right = deque()

n = int(input())

for _ in range(n):
    ins = list(input().split())

    if ins[0] == 'L':
        if left:
            right.append(left.pop())

    elif ins[0] == 'D':
        if right:
            left.append(right.pop())

    elif ins[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(ins[1])


print(''.join(left) + ''.join(reversed(right)))

