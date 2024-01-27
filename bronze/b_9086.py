import sys

n = int(input())
for _ in range(n):
    text = sys.stdin.readline().strip()
    print(text[0], text[-1], sep="")