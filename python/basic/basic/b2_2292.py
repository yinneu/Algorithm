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
## 최댓값이 언제까지인지 확인이 어려울 때는 while 문을 쓰는게 낫지,,