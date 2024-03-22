import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dic = dict()    
    total = 1

    for _ in range(n):
        c, t = input().split()
        if t in dic.keys(): # t in dic 과 동일
            dic[t] += 1
        else:
            dic[t] = 2
            
    lt = list(dic.values())
    for l in lt:
        total *= l
        
    print(total-1)