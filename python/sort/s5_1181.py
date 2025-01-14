# 중복 제거 set
import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(input().strip())

set_arr = list(set(arr))
set_arr.sort(key = lambda x: (len(x),x))

for s in set_arr:
    print(s)