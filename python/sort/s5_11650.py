import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    x, y = map(int, input().strip().split())
    arr.append((x, y))

# arr.sort(key = lambda x: (x[0], x[1])) 
# 정렬 기준을 주지 않아도 첫 번재 인자가 같은 경우, 오름차순으로 정렬됨 ㅇㅇ
arr.sort()

for a in arr:
    print(a[0], a[1])