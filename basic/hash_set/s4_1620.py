import sys
input = sys.stdin.readline

n, m = map(int,input().split())
st = {}

for i in range(1, n+1):
    s = input().strip()
    st[str(i)] = s
    st[s] = str(i)
    
for _ in range(m):
    print(st[input().strip()])