import sys
input = sys.stdin.readline

n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

for i in range(len(ns)):
    for j in range(i+1,len(ns)):
        if ns[i] > ns[j]:
            ns[i], ns[j] = ns[j], ns[i]

for i in ns:
    print(i)

