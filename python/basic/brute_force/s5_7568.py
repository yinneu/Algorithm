import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y, 1])
    

for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                arr[i][2] += 1
                
for v in arr:
    print(v[2], end=" ")