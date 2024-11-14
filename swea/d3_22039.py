#약 40m

T = int(input())

for _ in range(T):
    n = int(input())
    result = "impossible"
    if n > 1:
        m = n // 3
        d = n % 3
        
        if d == 0:
            result = "BBA" * m 
        elif d == 2:
            result = "BA" + ("BBA" * m)
            
    print(result)