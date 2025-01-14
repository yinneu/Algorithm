# 좌표정렬2
import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))
    
arr.sort(key = lambda x : (x[1], x[0]))

for a in arr:
    print(a[0], a[1])