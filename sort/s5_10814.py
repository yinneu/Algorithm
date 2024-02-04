import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    inp = input().strip().split()
    arr.append((int(inp[0]), inp[1]))

arr.sort(key = lambda x: (x[0]))

for a in arr:
    print(a[0],a[1])