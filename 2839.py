arr = []
n = int(input())

if n % 3 == 0:
    arr.append(n // 3)
if n % 5 == 0:
    arr.append(n // 5)
    
ft = n // 15
ftm = n % 15
for i in range(0,3):    
    if ftm > 5*i and (ftm - 5*i) % 3 == 0:
        arr.append(ft*3 + i + (ftm - 5*i) // 3)

if arr:
    print(min(arr))
else:
    print(-1)