H, M = map(int, input().split())

if M < 45:
    m = 15 + M
    if H != 0:
        h = H - 1
    else:
        h = 23
else:
    h = H
    m = M - 45
    
print(h, m)
    