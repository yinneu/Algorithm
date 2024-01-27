def func(a, b):
    result = pow(a, 2) - b ** 2
    return result

a, b = map(int, input().split())

print(func(a, b))