n, k = map(int, input().split())
ns = list(range(1, n+1))
result = []
index = 0
cnt = 1

while ns:
    if index > len(ns)-1:
        index = 0
    
    if cnt == k:
        result.append(ns.pop(index))
        cnt = 1
    else:
        cnt += 1
        index += 1

print('<', end="")
print(*result, sep=", ", end="")
print('>')

# print(f'<{", ".join(map(str, result))}>') => 이 방식이 더 좋을듯