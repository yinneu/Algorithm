# 좌표 압축
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().strip().split()))
srr = sorted(list(set(arr)))

dic = dict()
for i in range(0, len(srr)):
    dic[srr[i]] = i

for a in arr:
    print(dic[a], end=" ")