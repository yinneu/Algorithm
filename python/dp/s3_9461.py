# 파도반 수열
import sys
input = sys.stdin.readline
    
arr = [0] * 101
arr[1] = 1
arr[2] = 1
for i in range(3, 101):
    arr[i] = arr[i-3] + arr[i-2]

T = int(input())

for _ in range(T):
    n = int(input())
    print(arr[n])