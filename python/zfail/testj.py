arr = []
for _ in range(3):
    arr.append(int(input()))
    
if sum(arr) == 180:
    if arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
        if arr[0] == 60:
            print("Equilateral")
        else:
            print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
    