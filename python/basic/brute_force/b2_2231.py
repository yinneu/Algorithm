n = input()
N = int(n)

t = int(n[0])    # 최대 차이
for _ in range(len(n)-1):
    t += 9
    
minN = N - t
result = 0
for i in range(minN, N):
    Sum = i
    strN = str(i)
    for j in strN:
        Sum += int(j)
    if Sum == N:
        result = i
        break
        
print(result)