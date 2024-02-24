# 문제 제대로 읽기,,
import sys
input = sys.stdin.readline

arr = input().strip().split('-')
nm = []

for a in arr:
    pn = a.split('+')
    t = 0
    for n in pn:
        t += int(n)
    nm.append(t)
    
result = nm[0]
for i in range(1,len(nm)):
    result -= nm[i]
    
print(result)