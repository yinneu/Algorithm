import sys
input = sys.stdin.readline

n = int(input())
total = 0
for _ in range(n):
    flag = True
    check = [-1] * 26
    s = input().strip()
    
    for i in range(0, len(s)):
        j = ord(s[i])-97
        if check[j] != -1 and check[j] != i-1:  # 체크된 적이 없고, 연속되지 않는 경우
            flag = False
            break
        check[j] = i
    
    if flag:
        total += 1
        
print(total)