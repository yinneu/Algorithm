# 문제 조건을 파악하기
# 입력의 다양한 경우를 고려하기
import sys
input = sys.stdin.readline

arr = [0] * 257 
minh = 256
maxh = 0

n, m, b = map(int, input().split())
nm = n * m

for _ in range(n):
    lt = list(map(int,input().strip().split()))
    for l in lt:
        arr[l] += 1
        
        if minh > l:
            minh = l
        if maxh < l:
            maxh = l

if maxh != minh: # 주어진 땅이 이미 평평할 경우를 고려하기
    h = 0
    sec = nm * 256
    for i in range(minh, maxh+1):
        s = 0
        block = b
        for j in range(minh, maxh+1):
            if i < j:
                n = (j - i) * arr[j]
                s += (n * 2)
                block += n
            elif i > j:
                n = (i - j) * arr[j]
                s += n
                block -= n
        if block >= 0 and s <= sec: # 문제 조건! 같은 시간인 경우 땅 높이가 높은 것을 고르기
            sec = s
            h = i
else:
    sec = 0
    h = maxh
                
print(sec, h)