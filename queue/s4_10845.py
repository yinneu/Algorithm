import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    
    arr = list(input().strip().split())
    
    if len(arr) > 1:
        a.append(int(arr[1]))
    elif arr[0] == 'pop':
        if a:
            print(a.pop(0))
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(a))
    elif arr[0] == 'empty':
        if a:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if a:
            print(a[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if a:
            print(a[-1])
        else:
            print(-1)