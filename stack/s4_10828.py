#스택
import sys
input = sys.stdin.readline

n = int(input())
stk = []

for _ in range(n):
    tt = input().strip().split()
    
    if len(tt) > 1:
        stk.append(int(tt[1]))
    elif tt[0] == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif tt[0] == 'size':
        print(len(stk))
    elif tt[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    elif tt[0] == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)