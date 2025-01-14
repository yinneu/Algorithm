nums = [ int(input()) for i in range(10)]
result = []

for n in nums:
    t = n % 42
    if t not in result:
        result.append(t)
        
print(len(result))
