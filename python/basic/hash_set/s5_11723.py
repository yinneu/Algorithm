import sys
input = sys.stdin.readline

arr = [0] * 21
n = int(input())

for _ in range(n):
    s = input().strip().split()
    
    if len(s) > 1:
        i = int(s[1])
    
    if s[0] == 'add':        
        if arr[i] == 0:
            arr[i] = 1
    elif s[0] == 'remove':
        if arr[i] == 1:
            arr[i] = 0
    elif s[0] == 'check':
        print(arr[i])
    elif s[0] == 'toggle':
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0
    elif s[0] == 'all':
        for j in range(1, 21):
            if arr[j] != 1:
                arr[j] = 1
    elif s[0] == 'empty':
        arr = [0] * 21