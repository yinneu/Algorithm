arr = input()

flag = 1
if arr[1] == '0':
    flag = 2

print(int(arr[:flag]) + int(arr[flag:]))

