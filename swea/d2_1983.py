# sorted(list, key= lambda a = a[i], reverse= True/False)
T = int(input())

for t in range(1,T+1):

    #score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    n, k = map(int,input().split())
    stud = []

    for i in range(1, n+1):
        a, b, c = map(int, input().split())
        total = (a*0.35) + (b*0.45) + (c*0.2)
        stud.append((i, total))

    
    stst = sorted(stud, key=lambda a: a[1], reverse=True)

    iter = n // 10
    index = 0
    for i in range(n):
        if stst[i][0] == k:
            index = (i+1) / iter
            break

    if index <= 1:
        result = "A+"      
    elif index <= 2:
        result = "A0" 
    elif index <= 3:
        result = "A-" 
    elif index <= 4:
        result = "B+" 
    elif index <= 5:
        result = "B0" 
    elif index <= 6:
        result = "B-" 
    elif index <= 7:
        result = "C+"
    elif index <= 8:
        result = "C0"
    elif index <= 9:
        result = "C-"
    else:
        result = "D"

    print(f'#{t} {result}')
