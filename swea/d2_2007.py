# 패턴 마디 길이가 1일수도 있는데?
T = int(input())

for t in range(1, T+1):
    lt = input()
    cnt = 0
    for i in range(len(lt)): #시작
        start_ck = False
        for k in range(i+1, len(lt)):
            if lt[i] == lt[k]:
                flag = True
                cnt = 1
                for j in range(1, k-i):
                    if lt[i+j] != lt[k+j]:
                        flag=False
                        break
                    cnt += 1
                if flag:
                    start_ck = True
                    break
        if start_ck:
            break
        
    print(f'#{t} {cnt}')