import sys
input = sys.stdin.readline

arr = []
k, n = map(int, input().split())

for _ in range(k):
    arr.append(int(input()))
    
flag = sum(arr) // n
maxlen = 0 # max 길이

for i in range(flag, 0, -1):
    sm = 0
    for j in arr:    
        if j >= i:
            sm += (j // i)
    
    if sm >= n and i > maxlen:
        maxlen = i
        break
        
print(maxlen)