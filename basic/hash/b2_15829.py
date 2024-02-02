# 해시
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(ord,input().strip()))


result = 0
for i, v in enumerate(arr):
    result += (v-96) * pow(31, i)

print(result % 1234567891)