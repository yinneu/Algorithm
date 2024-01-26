import sys
input = sys.stdin.readline() # 입력이 많을 때

result = 1
n = int(input)

if n == 0:
    print(1)
else:
    for i in range(1, n+1):
        result *= i
    print(result)