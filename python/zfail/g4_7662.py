import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    q = [] 
    for _ in range(k):
        a, n = input().strip().split()
        n = int(n)
        if a == 'I':
            q.append(n)
            q.sort()
        elif a == 'D':
            if q:
                if n == 1:
                    q.pop()
                else:
                    q.pop(0)

    if q:
        print(q[-1], q[0])
    else:
        print("EMPTY")   