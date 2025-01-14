n = int(input())
cnt = 0

for i in range(1, n+1):
    if i % 5 == 0:
        t = i
        while t % 5 == 0:
            cnt += 1
            t /= 5
        
print(cnt)

# 5의 개수 만큼 10이 만들어지니까~