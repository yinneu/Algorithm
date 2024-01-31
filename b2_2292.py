n = int(input())
pre = 1

for i in range(1, 1000000): 
    if n == 1:
        print(1)
        break
        
    if pre < n and n <= pre + (6 * i):       
        print(1 + i)
        break
    
    pre += (6 * i)
    
    
## 최소 최대 조건 확인을 해야한다.