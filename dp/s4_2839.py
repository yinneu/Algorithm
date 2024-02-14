## 다이나믹 프로그래밍 , 그리디 알고리즘,, => 으로 푸는 방식 ^^
arr = []
n = int(input())

n1 = n // 5
n2 = n // 3

for i in range(0,n1+1):
    for j in range(0,n2+1):
        if n == (5*i + 3*j):
            arr.append(i+j)
if arr:
    print(min(arr))
else:
    print(-1)