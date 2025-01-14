# 조합
# 이항 계수 : 주어진 집합에서 순서상관없이 원하는 개수만큼 뽑을 때의 경우의 수, 뽑는다, 뽑지 않는다 두 가지 경우만 있어서 이항 계수라 함.
# n! / (n-k)! k!

def fac(i):
    r = 1
    for i in range(i, 0, -1):
        r *= i
    return r

n, k = map(int, input().split())
result = fac(n) // (fac(n-k) * fac(k))

print(result)