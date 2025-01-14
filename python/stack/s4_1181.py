# 조건에 잘맞게 짜기,, 기본 리스트를 사용해도 상관없음 ㅇㅇ
# 문자열은 리스트로 변환안해도 ㅇㅇ
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