n = int(input())
i = 0
while n > 0: 
    i += 1
    n -= i
    
a = i + n
b = 1 - n

if i % 2:
    print(f'%d/%d' %(b,a))
else:
    print(f'%d/%d' %(a,b))