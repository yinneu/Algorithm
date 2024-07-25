maxp = 0
person = 0

for _ in range(10):
    a, b = map(int, input().split())
    person = person - a + b
    
    if person > maxp:
        maxp = person
    
print(maxp)