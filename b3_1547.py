n = int(input())

arr = [False, True, False, False]

for i in range(n):
    x, y = map(int, input().split())

    if arr[x] or arr[y]:
        arr[x], arr[y] = arr[y], arr[x]

for i in range(4):
    if arr[i]:
        print(i)
        break
