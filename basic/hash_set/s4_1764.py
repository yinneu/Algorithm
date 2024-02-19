#듣보잡 #집합
import sys
input = sys.stdin.readline

h = set()
s = set()

n, m = map(int, input().split())

for _ in range(n):
    h.add(input().strip())

for _ in range(m):
    s.add(input().strip())
    
hs = list(h & s)
hs.sort()

print(len(hs))
for o in hs:
    print(o)