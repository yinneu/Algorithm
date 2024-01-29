sosu = [2, 3, 5, 7, 11, 13]

for i in range(17, 101):
    flag = False
    for j in sosu:
        if i % j == 0:
            flag = True
    if not flag:
        sosu.append(i)

n = int(input())
nums = map(int, input().split())
cnt = 0

for i in nums:
    flag = False
    if i == 1:
        continue
    for j in sosu:
        if i % j == 0 and i not in sosu:
            flag = True
    if not flag:
        cnt += 1
            
print(cnt)

## 이미 구한 소수는 제외하고 나눴어야 했는데,,, 소수로 소수를 나누어서 계속 틀림..
## 숫자는 최대 1000까지이니까 두 자리 수 소수까지만 구하고 찾는 방식을 사용하였음.
## 리스트가 큰 경우 set로 변환하여 탐색하면 평균 시간 복잡도 O(1)으로 탐색 가능함.