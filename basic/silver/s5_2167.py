import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    arr.append(row)

    
k = int(input())
for _ in range(k):
    n, m, dn, dm = map(int, input().split())
    
    total = 0
    for i in range(n-1, dn):
        for j in range(m-1, dm):
            total += arr[i][j]        
    print(total)