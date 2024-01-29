s, m, total = map(int, input().split())

day = s - m

if total % day == 0:
    n = total // day
    # temp = (day * n-1) + s
    temp = (day * n-1) + 1
    result = n - m
    # temp = (total - (day * (n-1))) / day
    # if temp % 

else:
    n = total // day + 1
    result = n
    
print(result)