# stack에 요소가 있고, 마지막 요소와 현재 값이 같을 때만 pop 이외에는 append
# 코드 먼저 쓰지말고, 로직을 먼저 구상하고 하기~

n = int(input())
cnt = 0

for _ in range(n):
    lt = []
    
    st = input()
    
    for i in range(len(st)):
        if not lt:
            lt.append(st[i])
        else:
            if lt[-1] != st[i]:
                lt.append(st[i])
            else:
                lt.pop()
        
        # if lt and lt[-1] == st[i]:
        #   lt.pop()
        # else:
        #   lt.append()
            
    if not lt:
        cnt += 1
        
print(cnt)