import sys
input = sys.stdin.readline

n = int(input())
re = 1
for i in range(2, n+1):
    re *= i

print(re)