import sys
input = sys.stdin.readline

n = int(input())
trr = []
result = []

for _ in range(n):
    a, b = map(int,input().split())
    trr.append((a,b))
    
trr.sort(key= lambda x : (x[1], x[0])) # 끝나는 시간, 시작 시간

for t in trr:
    if not result:
        result.append(t)
    else:
        if result[-1][1] <= t[0]: # 이전 회의 끝나는 시간보다 회의 시작 시간이 같거나 느린 경우
            result.append(t)

print(len(result))