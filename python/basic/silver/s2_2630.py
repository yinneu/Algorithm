# 재귀, 분할정복
from collections import deque
import sys
input = sys.stdin.readline

def scan(n, m, k):
    t = arr[n][m]
    for i in range(n, n+k):
        for j in range(m, m+k):
            if arr[i][j] != t:
                return -1
    return t

def cal(N):
    result = [0, 0]
    deq = deque([(0,0,N)])
    while deq:
        n, m, k = deq.popleft()
        r = scan(n, m, k)
        if r == -1:
            k = k//2
            for lt in [(0,0), (k, 0), (0, k), (k, k)]:
                deq.append([n+lt[0], m+lt[1], k])
        else:
            result[r] += 1
    return result

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        a = list(map(int,input().strip().split()))
        arr.append(a)
        
    result = cal(N)
    for p in result:
        print(p)