# 계수 정렬으로 풀었을때 틀림.
# 데이터 범위가 거의 백만이라 적합하지 않은 듯 함.
# 병렬 정렬 기반인 sort를 사용
import sys
input = sys.stdin.readline

a =[]
n = int(input())

for _ in range(n):
    a.append(int(input()))
    
a.sort()

for i in a:
    print(i)