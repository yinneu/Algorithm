#8:07
n = int(input())

lt = ['3', '6', '9']
for i in range(1, n+1):
    slt = str(i)
    flag = False

    for s in slt:
        if s in lt:
            print('-', end="")
            if not flag:
                flag = True

    if flag:
        print("", end=" ")
    else:
        print(i, end=" ")