import sys
input = sys.stdin.readline

dic = {}
n, m = map(int, input().split())

for _ in range(n):
    s, k = input().split()
    dic[s] = k

for _ in range(m):
    print(dic[input().strip()])