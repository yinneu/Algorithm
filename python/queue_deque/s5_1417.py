import sys
input = sys.stdin.readline

n = int(input())
dasom = int(input())
lt = []
cnt = 0

for i in range(1,n):
    num = int(input())
    lt.append(num)
    
lt.sort(reverse=True)
    
while lt:
    m = lt.pop(0)
    if dasom <= m:
        dasom += 1
        m -= 1
        cnt += 1
        if dasom <= m:
            for i in range(len(lt)):
                if lt[i] <= m:
                    lt.insert(i, m)
                    break
            else:
                lt.append(m)

print(cnt)            