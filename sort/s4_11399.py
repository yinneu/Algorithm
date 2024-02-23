import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

s = 0
t = 0
for i in arr:
    t += i
    s += t
print(s)