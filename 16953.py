## A -> B 를 만드는 연산 수의 최솟값.


def AToB(num, target):
    count = -2
    from collections import deque
    deq = deque()
    deq.append((num, 0))

    while deq:
        n, cnt = deq.popleft()
        if n == target:
            count = cnt
            break
        elif n < target:
            in1 = int(str(n)+'1')
            deq.append((n*2, cnt+1))
            deq.append((in1, cnt+1)) 

    return count

a, b = map(int, input().split())
result = AToB(a, b)+1
print(result)


