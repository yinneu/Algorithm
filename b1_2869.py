a, b, v = map(int, input().split())

t1 = v - a
t2 = a - b

if t1 == 0 :
    print(1)
else:
    if t1 % t2 != 0:
        print(t1 // t2 + 2)
    else:
        print(t1 // t2 + 1)