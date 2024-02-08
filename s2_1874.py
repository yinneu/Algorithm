# 스택수열
# i 증가, a > i 크다면 i ++ push
# 중복되는 연산이 많음. 좀 더 간결하게 로직써서 하면 좋을듯
# 같거나 작을때까지 while로 push 후, a와 i가 같으면 pop() 가능, 아니면 no => 다음 수열 값이 마지막으로 넣은 값과 같아야하기 때문
from collections import deque
import sys
input = sys.stdin.readline

arr = []
result = deque()
deq = deque()

n = int(input())
for _ in range(n):
    arr.append(int(input()))

i = 1
flag = True
for a in arr:
    while True:
        if a > i:
            deq.append(i)
            result.append('+')
            i += 1
            
        elif a == i:
            deq.append(i)
            result.append('+')
            i += 1
            
            deq.pop()
            result.append('-')
            break
            
        else:
            dpop = deq.pop()
            result.append('-')
            if dpop == a:
                break
            else:
                flag = False
                break
                
if flag:
    for r in result:
        print(r)
else:
    print("NO")