import sys
import math
input = sys.stdin.readline

n = int(input())

arr = [0] * (n+1)
arr[0] = 1
arr[1] = 1

if n > 1:
    for i in range(2, n+1):
        arr[i] = (arr[i-2] * 2) + arr[i-1]

print(arr[n]%10007)
    
    

# 조합
# c = n // 2
# m = n % 2
# cnt = 0

# for i in range(c+1):
#     one = 2*i + m
#     t = c + i + m
#     T = math.comb(t, one)
#     for j in range(c-i+1):
#         P = math.comb(c-i, j)
#         cnt += (T * P)

# print(cnt%10007)