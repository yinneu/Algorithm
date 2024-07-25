input()
arr = list(map(int, input().split()))

check = 0
total = 0

for i in arr:
    if i == 1:
        check += 1
        total = total + check
    else:
        check = 0 
        
print(total)