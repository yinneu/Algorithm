# 최소 3자리, 666만 포함되어있으면 되므로 다른 추가적인 건 필요없음,,
n = int(input())

i = 666
cnt = 0
result = 0
while cnt < n:
    if '666' in str(i):
        cnt += 1
        result = i
    i += 1
print(result)