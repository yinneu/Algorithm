import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

s = input().strip()
arr = s.split('I')
print(arr)

if s[0] == 'I':
    start = 0
else:
    start = 1

result = 0
cnt = 0
for i in range(start, len(arr)):
    if arr[i] == 'O':
        cnt += 1
        if cnt == N:
            result += 1
            cnt = 0
    else:
        cnt = 0

