import sys
input = sys.stdin.readline

while True:
    
    n = input().strip()
    
    if n == '0':
        break
        
    cnt = 1    
    for i in range(0, len(n)):
        if n[i] == '0':
            cnt += 5
        elif n[i] == '1':
            cnt += 3
        else:
            cnt += 4         
    print(cnt)