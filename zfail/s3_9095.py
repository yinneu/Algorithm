import sys
input = sys.stdin.readline

arr = [1] * 11

# 한가지
for i in range(1,11):
    # 한가지
    for j in [2,3]:
        if i % j == 0:
            arr[i] +=1
    
    # 두가지
    lt = [(1,2),(1,3),(2,3)]
    for l in lt:
        if l[0] * 1
    


# T = int(input())

# for _ in range(T):
#     n = int(input())
#     print(n)
    
#     case = 1 # 경우의 수 (1로만 만들어지는 경우 포함)
    
    
#     # 한 가지 수
#     for i in [2,3]:
#         if ()



def cal(n):
    
    if n < 1:
        return 0
    
    cal(n-3)
    cal(n-2)
    cal(n-1)