n = int(input())
s = list(map(int, input().split()))

maxN = max(s)
sumN = 0

for i in s:
    if i != 0:
        sumN += i / maxN * 100
        
print(sumN / n)