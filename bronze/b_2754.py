s = input()

if s[0] == 'F':
    print(0.0)
else:   
    if s[0] == 'A':
        n = 4.0
    elif s[0] == 'B':
        n = 3.0
    elif s[0] == 'C':
        n = 2.0
    elif s[0] == 'D':
        n = 1.0

    if s[1] == '+':
        print(n+0.3)
    elif s[1] == '0':
        print(n)
    elif s[1] == '-':
        print(n-0.3)