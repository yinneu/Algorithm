#약 40m

T = int(input())

type1 = "BA" # 나머지 2
type2 = "BB" # 나머지 0

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