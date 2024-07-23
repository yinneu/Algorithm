n = int(input())

dic = dict()

for _ in range(n):
    name = input()
    if name[0] in dic:
        dic[name[0]] += 1
    else:
        dic[name[0]] = 1

lt = list(dic.items())
result = []

for i in lt:
    if i[1] >= 5:
        result.append(i[0])

if result:
    result.sort()
    for i in result:
        print(i, end="")
else:
    print("PREDAJA")
