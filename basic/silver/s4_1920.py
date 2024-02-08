# 해쉬, 사전으로 저장해서 찾기 or if v in list? -> 시간초과 날듯
# 집합 안에 넣기, m 값들이 있는지 없는지만 검사하면 되므로 탐색 시간이 O(1)인 집합 사용
import sys
input = sys.stdin.readline

input()
A = set(input().strip().split())

input()
arr = input().strip().split()

for m in arr:
    if m in A:
        print(1)
    else:
        print(0)