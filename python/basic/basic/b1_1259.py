import sys
input = sys.stdin.readline

while True:
    t = input().strip()    
    if t == '0':
        break
        
    n = len(t) // 2
    result = 'yes'
    
    for i in range(0, n):
        if t[i] != t[-(i+1)]:
            result = 'no'
            break
            
    print(result)