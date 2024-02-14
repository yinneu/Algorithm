#https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
# 에라토스테네스의 체
import sys
input = sys.stdin.readline

def sol(x):
    arr = [True for _ in range(x+1)]
    arr[0] = False
    arr[1] = False
    
    for i in range(2, x+1):
        if arr[i]: # i가 소수이면
            for j in range(i*2, x+1, i): # i의 배수를 모두 False
                arr[j] = False
    return arr
    

m, n = map(int, input().split())

arr2 = sol(n)

for i in range(m, n+1):
    if arr2[i]:
        print(i)