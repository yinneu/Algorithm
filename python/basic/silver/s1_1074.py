import sys
input = sys.stdin.readline

def cal(y, x, n, r, c):
    if n == 1:
        if y == r:
            if x == c:
                return 0
            else:
                return 1
        else:
            if x == c:
                return 2
            else:
                return 3
    
    to = 2**(n-1)
    if r < y+to and c < x+to: #1번
        return cal(y, x, n-1, r, c)
    elif r < y+to:           # 2번
        return cal(y, x+to, n-1, r, c) + to * to
    elif c < x+to:            # 3번
        return cal(y+to, x, n-1, r, c) + to * to * 2
    else:                   # 4번
        return cal(y+to, x+to, n-1, r, c) + to * to * 3

n, r, c = map(int, input().split())
print(cal(0, 0, n, r, c))