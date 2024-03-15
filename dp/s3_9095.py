# dp, a(n) = a(n-1) + a(n-2) + a(n-3) # 1 더한 조합 + 2를 더한 조합 + 3을 더한 조합
import sys
input = sys.stdin.readline

arr = [0, 1, 2, 4]
for i in range(4, 11):
    n = arr[i-3] + arr[i-2] + arr[i-1]
    arr.append(n)

T = int(input())
for _ in range(T):
    m = int(input())
    print(arr[m])